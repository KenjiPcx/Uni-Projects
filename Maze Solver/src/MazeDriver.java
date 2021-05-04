import maze.Maze;
import maze.routing.*;

/**
 * Driver program to help with the development of the logic of
 * the route finder. 
 * Used to print the states of maze and route finder.
 */
public class MazeDriver {
    public static void main(String args[]) {
        Maze m = Maze.fromTxt("./resources/mazes/maze5.txt");
        RouteFinder rf = new RouteFinder(m);
        
        boolean done = false;
        int i = 1;
        do {
            System.out.println("Step " + i + "\n");
            done = rf.step();
            i += 1;
        } while (!done);
        System.out.println(rf.getRoute());
    }
}
