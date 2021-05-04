package maze.routing;

import maze.*;

import java.util.Stack;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

/**
 * Contains the state and logic of solving a maze
 */
public class RouteFinder implements Serializable {
    private Maze maze;
    private Stack<Tile> route;
    private Stack<List<Maze.Direction>> directions;
    private Stack<Tile> branchTiles;
    private Tile lastTile;
    private Tile currentTile;
    private Tile nextTile;
    private boolean undoMode;
    private boolean restartMode;
    private boolean finished;
    private String status;
    private Stack<Tile> abandonedTiles;
    private int noOfSteps;

    /**
     * Initializes an instance of a route finder for the given maze.
     * @param m: Maze
     */
    public RouteFinder(Maze m) {
        this.maze = m;
        this.route = new Stack<Tile>();
        this.directions = new Stack<List<Maze.Direction>>();
        this.branchTiles = new Stack<Tile>();
        this.lastTile = null;
        this.currentTile = null;
        this.nextTile = null;
        this.undoMode = false;
        this.restartMode = false;
        this.finished = false;
        this.status = "Start";
        this.abandonedTiles = new Stack<Tile>();
        this.noOfSteps = 0;
    }

    /**
     * Gets the maze that belongs to the route finder.
     * @return Returns the maze that belongs to the route finder
     */
    public Maze getMaze() {
        return this.maze;
    }

    /**
     * Gets the current route of the maze found by the route finder. 
     * @return Returns the current route found by the route finder
     */
    public List<Tile> getRoute() {
        return this.route;
    }

    /**
     * Checks if the route finding process is finished.
     * @return Returns true if route finding process is finished, false otherwise
     */
    public boolean isFinished() {
        return this.finished;
    }

    /**
     * Loads an instance of a route finder from a saved file.
     * @param filepath: File path
     * @return Returns the instance of route finder from the saved file, returns null if file does not exist
     */
    public static RouteFinder load(String filepath) {
        try (FileInputStream fileInputStream = new FileInputStream(filepath);) {
            try (ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);) {
                return (RouteFinder) objectInputStream.readObject();
            }
        } catch (IOException | ClassNotFoundException e) {
            System.out.println("File " + filepath +  " is invalid");
        } 
        return null;
    }

    /**
     * Serializes the instance of a route finder and save to a file.
     * @param filepath: File path
     */
    public void save(String filepath) {
        try (FileOutputStream fileOutputStream = new FileOutputStream(filepath);) {
            try (ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream)) {
                objectOutputStream.writeObject(this);
                objectOutputStream.flush();
            }
        } catch (IOException e) {
            System.out.println("File " + filepath +  " is invalid");
        }
    }

    /**
     * Steps through the maze solving by one step each time the function is called.
     * @return Returns true if the maze solving process is finished, false otherwise
     * @throws NoRouteFoundException if a route cannot be found for the maze (all potential routes exhausted)
     */
    public boolean step() throws NoRouteFoundException {
        this.noOfSteps += 1;
        String noRouteErr = "There is no route for this maze";

        // Start condition
        if (this.route.isEmpty()) {
            this.currentTile = this.maze.getEntrance();
            this.route.push(this.maze.getEntrance());

        // Finish condition
        } else if (this.finished) {
            return true;
        
        // Alternate finish condition
        } else if (this.currentTile == this.maze.getExit()) {
            if (this.route.peek() == this.maze.getExit()) {
                this.status = "Done";
            }
            this.finished = true;
            return true;

        // Step Procedure
        } else if (!this.undoMode && !this.restartMode) {
            int noOfRoute = 0;
            int noOfWall = 0;
            Tile adjTile;
            Maze.Direction revD = null;
            ArrayList<Maze.Direction> dir = new ArrayList<Maze.Direction>();

            // Tile Checks
            for (Maze.Direction d : Maze.Direction.values()) {
                adjTile = this.maze.getAdjacentTile(this.currentTile, d);

                // Check Exit is adjacent
                if (adjTile == this.maze.getExit()) {
                    this.route.push(adjTile);
                    this.currentTile = adjTile;
                    this.finished = true;
                    this.status = "Found Exit! Done";
                    return true;
                }

                // Check for navigable tile
                if (adjTile != null && adjTile.isNavigable()) {
                    if (adjTile != this.lastTile) {
                        noOfRoute += 1;
                        dir.add(d);
                    } else if (adjTile == this.lastTile) {
                        revD = d;
                    }
                } else if (adjTile == null || !adjTile.isNavigable()) {
                    noOfWall += 1;
                    if (noOfWall == 4) {
                        throw new NoRouteFoundException(noRouteErr);
                    }
                }
            }

            // Dead end
            if (noOfRoute == 0) {
                this.undoMode = true;
                this.status = "Dead End";
                this.undoStep();

            // Normal tiles and Branch Tiles
            } else {
                Maze.Direction d = dir.get(0);
                this.nextTile = this.maze.getAdjacentTile(this.currentTile, d);
                this.status = "Going " + d + " From " + this.maze.getTileLocation(this.currentTile) 
                                + " to " + this.maze.getTileLocation(this.nextTile);

                // Check if visited before
                if (!this.route.contains(this.nextTile)) {
                    this.route.push(this.nextTile);

                    // Set branch tile
                    if (noOfRoute > 1) {
                        dir.remove(0);
                        if (revD != null) {
                            dir.add(revD);
                        }
                        if (!this.branchTiles.contains(this.currentTile)) {
                            this.directions.push(dir);
                            this.branchTiles.push(this.currentTile);
                        }
                    }
                    // Update Tiles
                    this.lastTile = this.currentTile;
                    this.currentTile = this.nextTile;

                // Visited path before
                } else {
                    this.status = "Visited " + this.maze.getTileLocation(this.nextTile) + " before";
                    this.undoMode = true;
                    this.undoStep();
                }
            }

        } else if (this.undoMode) {
            this.undoStep();

        } else if (this.restartMode) {
            this.restartStep();
        }
        // this.printStates();
        return false;
    }

    /**
     * Helper method to undo steps taken
     */
    public void undoStep() {
        String noRouteErr = "There is no route for this maze";

        // Undo last step
        this.status = "Undoing last step" +
        " Going back to " + this.maze.getTileLocation(this.lastTile);

        // Update Tiles
        // Popping empty stack means all routes are tried
        try {
            this.abandonedTiles.add(this.route.pop());
            this.currentTile = this.route.pop();
            if (this.route.isEmpty()) {
                this.route.push(this.maze.getEntrance());
                this.lastTile = null;
            } else {
                this.lastTile = this.route.peek();
                this.route.push(this.currentTile);
            }
        } catch (IndexOutOfBoundsException e) {
            this.status = noRouteErr;
            throw new NoRouteFoundException(noRouteErr);
        }

        // Check if currentTile is at a branchTile
        if (this.branchTiles.isEmpty()) {
            this.status = noRouteErr;
            throw new NoRouteFoundException(noRouteErr);
        } else if (this.currentTile == this.branchTiles.peek()) {
            this.undoMode = false;
            this.restartMode = true;
        }
    }

    /**
     * Stops undoing steps and restarts the step process to find unvisited paths 
     */
    public void restartStep() {
        String noRouteErr = "There is no route for this maze";
        if (this.currentTile == this.maze.getEntrance() && this.directions.isEmpty()) {
            this.status = noRouteErr;
            throw new NoRouteFoundException(noRouteErr);
        }
        List<Maze.Direction> dir = new ArrayList<Maze.Direction>();
        dir = this.directions.pop();

        // Check if the only way left is backwards
        if (dir.size() == 1 && this.currentTile != this.maze.getEntrance()) {
            this.status = "Undoing last step" + 
                          " Going back to " + this.maze.getTileLocation(this.lastTile);
            
            // Update Tiles
            // Popping empty stack means all routes are tried
            try {
                this.abandonedTiles.add(this.route.pop());
                this.currentTile = this.route.pop();
                if (this.route.isEmpty()) {
                    this.lastTile = null;
                } else {
                    this.lastTile = this.route.peek();
                }
                this.route.push(this.currentTile);
            } catch (IndexOutOfBoundsException e) {
                throw new NoRouteFoundException(noRouteErr);
            }

            if (!this.branchTiles.contains(this.maze.getEntrance()) && this.currentTile == this.maze.getEntrance()) {
                throw new NoRouteFoundException(noRouteErr);

            // For normal tiles behind branch tiles
            } else if (!this.branchTiles.contains(this.currentTile)) {
                this.undoMode = true;
                this.restartMode = false;
                this.branchTiles.pop();
            // For consecutive branch tiles
            } else if (this.branchTiles.contains(this.currentTile)) {
                this.branchTiles.pop();
            }

        // Exhausted all routes
        } else if (this.currentTile == this.maze.getEntrance() && dir.isEmpty()) {
            throw new NoRouteFoundException(noRouteErr);
        
        // Found unvisited path
        } else {
            this.nextTile = this.maze.getAdjacentTile(this.currentTile, dir.get(0));
            this.status = "Found unvisited path at " + this.maze.getTileLocation(this.currentTile) +
                          " Going " + dir.get(0) + " to " + this.maze.getTileLocation(this.nextTile);
            dir.remove(0);
            if (this.currentTile != this.maze.getEntrance()) {
                this.directions.push(dir);
            }
            this.route.push(this.nextTile);
            this.lastTile = this.currentTile;
            this.currentTile = this.nextTile;
            this.restartMode = false;
        }
    }

    /**
     * Prints out the states of the maze and route finder
     */
    public void printStates() {
        // States
        System.out.println(this.status);
        // System.out.println(this.toString());
        System.out.println("Route: " + this.route ); //+ this.maze.getTileLocation(this.route.peek())
        System.out.println("BranchTiles: " + this.branchTiles);
        System.out.println("Directions: " + this.directions);
        System.out.println("CurrentTile: " + this.currentTile);
        System.out.println("CurrentTile Coords: " + this.maze.getTileLocation(this.currentTile));
        System.out.println("LastTile: " + this.lastTile);
        System.out.println("LastTile Coords: " + this.maze.getTileLocation(this.lastTile));
        System.out.println("UndoMode: " + this.undoMode);
        System.out.println("RestartMode: " + this.restartMode + "\n");
    }
    
    /**
     * Returns the string representation of the maze and current route.
     * @return Returns the string representation of the maze and the current route
     */
    public String toString() {
        StringBuilder s = new StringBuilder();
        int mazeSize = this.maze.getTiles().size()-1;
        for (int i=0; i<this.maze.getTiles().size(); i++) {
            if (mazeSize >= 10) {
                if (mazeSize-i < 10) {
                    s.append(" " + Integer.toString(this.maze.getTiles().size()-i-1) + "  ");
                } else {
                    s.append(Integer.toString(this.maze.getTiles().size()-i-1) + "  ");
                }
            } else {
                s.append(Integer.toString(this.maze.getTiles().size()-i-1) + "  ");
            }
            for (Tile col : this.maze.getTiles().get(i)) {
                if (this.route.contains(col)) {
                    s.append(" -");
                } else if (this.abandonedTiles.contains(col)) {
                    s.append(" =");
                } else {
                    s.append(" " + col.toString());
                }
            }
            s.append("\n");
        }
        if (mazeSize >= 10) {
            s.append("\n    "); 
        } else {
            s.append("\n   "); 
        }
        for (int i=0; i<this.maze.getTiles().get(0).size(); i++) {
            s.append(" " + Integer.toString(i));
        }
        s.append("\n");
        return s.toString();
    }

    /**
     * Gets the current status of the route finder.
     * @return Returns the current status of the route finder
     */
    public String getStatus() {
        return this.status;
    }


    /**
     * Gets the total number of steps
     * @return Returns the total number of steps
     */
    public int getNoOfSteps() {
        return this.noOfSteps;
    }
}
