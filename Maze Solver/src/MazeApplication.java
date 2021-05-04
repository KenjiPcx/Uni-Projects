import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.layout.*;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuItem;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.MenuBar;
import maze.InvalidMazeException;
import maze.Maze;
import maze.routing.NoRouteFoundException;
import maze.routing.RouteFinder;
import maze.visualization.MazeWithCoordinateGraphics;
import maze.visualization.TileLegend;
import maze.visualization.AppLabel;
import maze.visualization.AlertBox;
import java.nio.file.Paths;
import java.io.File;

/**
 * Contains the settings and logic for the GUI of the Maze application
 */
public class MazeApplication extends Application {

    private RouteFinder routefinder;
    private MazeWithCoordinateGraphics mazegraphics;

    /**
     * Contains the settings of the GUI of the Maze application
     */
    @Override
    public void start (Stage stage) throws Exception {

        Scene mainMenuScene;
        Scene appScene;
        String initialStatus = "Status: \nNot Started Yet";
        

        // Main App Layouts
        BorderPane root = new BorderPane();
        ScrollPane scrollPane = new ScrollPane();
        VBox layout = new VBox(30);
        layout.setAlignment(Pos.CENTER);
        HBox container = new HBox(85);
        container.setAlignment(Pos.CENTER);
        this.mazegraphics = new MazeWithCoordinateGraphics(30);
        HBox topBtns = new HBox(30);
        topBtns.setAlignment(Pos.CENTER);
        VBox stepBtns = new VBox(50);
        stepBtns.setAlignment(Pos.CENTER);
        TileLegend legendBar = new TileLegend(30);
        legendBar.setMaxWidth(120);
        legendBar.setMinHeight(150);
        legendBar.setAlignment(Pos.CENTER);
        legendBar.setId("sideRectangles");
        VBox legendBarContainer = new VBox(legendBar);
        legendBarContainer.setMinWidth(150);
        legendBarContainer.setAlignment(Pos.CENTER);
        legendBarContainer.setId("sidebar");


        // Label
        AppLabel mainLabel = new AppLabel("Maze Solver", 45);
        VBox.setMargin(mainLabel, new Insets(0, 0, 40, 0));
        AppLabel statusLabel = new AppLabel(initialStatus, 15);
        VBox.setMargin(statusLabel, new Insets(20, 0, 0, 50));
        statusLabel.setPrefHeight(50);
        statusLabel.setId("botbar");
        AppLabel noOfSteps = new AppLabel("Number of\nSteps: ", 15);


        // Top Buttons
        Button loadMapBtn = new Button("Load Map");
        loadMapBtn.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Load File");
            fileChooser.setInitialDirectory(Paths.get("./resources/mazes").toFile());
            File file;
            try {
                file = fileChooser.showOpenDialog(stage); 
            } catch (IllegalArgumentException err) {
                fileChooser.setInitialDirectory(Paths.get(".").toFile());
                file = fileChooser.showOpenDialog(stage); 
            }
            if (file != null) {
                try {
                    this.routefinder = new RouteFinder(Maze.fromTxt(file.toString()));
                    this.mazegraphics.setMaze(this.routefinder.toString());
                    this.mazegraphics.updateGraphics();
                    noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                    statusLabel.setText(initialStatus);
                } catch (InvalidMazeException err) {
                    AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                    alertBox.showAndWait();
                }
            }
        });
        Button loadRouteBtn = new Button("Load Route");
        loadRouteBtn.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Load File");
            fileChooser.setInitialDirectory(Paths.get(".").toFile());
            File file = fileChooser.showOpenDialog(stage); 
            if (file != null) {
                this.routefinder = RouteFinder.load(file.toString());
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateGraphics();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            }
        });
        Button saveRouteBtn = new Button("Save Route");
        saveRouteBtn.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Save File");
            fileChooser.setInitialDirectory(Paths.get(".").toFile());
            File file = fileChooser.showSaveDialog(stage);
            if (file != null) {
                this.routefinder.save(file.toString());
            }
        });
        topBtns.getChildren().addAll(loadMapBtn, loadRouteBtn, saveRouteBtn);

        
        // Right Buttons 
        VBox stepLabelContainer = new VBox(noOfSteps);
        stepLabelContainer.setAlignment(Pos.CENTER);
        stepLabelContainer.setId("sideRectangles"); 
        stepLabelContainer.setMaxWidth(100);
        Button stepBtn = new Button("Step");
        stepBtn.setOnAction(e -> {
            try {
                this.routefinder.step();
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateMaze();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            } catch (NoRouteFoundException err) {
                statusLabel.setText("Status: " + this.routefinder.getStatus());
                AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                alertBox.showAndWait();
            }
        });
        ChoiceBox customStepVal = new ChoiceBox<Integer>();
        for (int i=1;i<11;i++) {
            customStepVal.getItems().add(Integer.valueOf(i));
        }
        Button customStepBtn = new Button("Step");
        customStepBtn.setOnAction(e -> {
            Integer n = (Integer)customStepVal.getValue();
            try {
                for (int i=0;i<n.intValue();i++) {
                    this.routefinder.step();
                }
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateMaze();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            } catch (NoRouteFoundException err) {
                statusLabel.setText("Status: " + this.routefinder.getStatus());
                AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                alertBox.showAndWait();
            }
        });
        Button skipStepsBtn = new Button("Skip");
        skipStepsBtn.setOnAction(e -> {
            try {
                boolean done;
                do {
                    done = this.routefinder.step();
                } while (!done);
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateMaze();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            } catch (NoRouteFoundException err) {
                statusLabel.setText("Status: " + this.routefinder.getStatus());
                AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                alertBox.showAndWait();
            }
        });
        HBox customBtnWrapper = new HBox(0);
        customBtnWrapper.setAlignment(Pos.CENTER);
        customBtnWrapper.getChildren().addAll(customStepVal, customStepBtn);
        stepBtns.getChildren().addAll(stepBtn, customBtnWrapper, skipStepsBtn, stepLabelContainer);
        stepBtns.setMinWidth(150);
        stepBtns.setId("sidebar");


        // Menu
        Menu fileMenu = new Menu("File");
        MenuItem fm1 = new MenuItem("Load Text");
        fm1.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Load File");
            fileChooser.setInitialDirectory(Paths.get("./resources/mazes").toFile());
            File file;
            try {
                file = fileChooser.showOpenDialog(stage); 
            } catch (IllegalArgumentException err) {
                fileChooser.setInitialDirectory(Paths.get(".").toFile());
                file = fileChooser.showOpenDialog(stage); 
            }
            if (file != null) {
                try {
                    this.routefinder = new RouteFinder(Maze.fromTxt(file.toString()));
                    this.mazegraphics.setMaze(this.routefinder.toString());
                    this.mazegraphics.updateGraphics();
                    noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                    statusLabel.setText("Status: \n" + this.routefinder.getStatus());
                } catch (InvalidMazeException err) {
                    AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                    alertBox.showAndWait();
                }
            }
        });
        MenuItem fm2 = new MenuItem("Load Route");
        fm2.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Load File");
            fileChooser.setInitialDirectory(Paths.get(".").toFile());
            File file = fileChooser.showOpenDialog(stage); 
            if (file != null) {
                this.routefinder = RouteFinder.load(file.toString());
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateGraphics();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            }
        });
        MenuItem fm3 = new MenuItem("Save Route");
        fm3.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Save File");
            fileChooser.setInitialDirectory(Paths.get(".").toFile());
            File file = fileChooser.showSaveDialog(stage);
            if (file != null) {
                this.routefinder.save(file.toString());
            }
        });
        MenuItem fm4 = new MenuItem("Exit");
        fm4.setOnAction(e -> {
            stage.close();
        });
        fileMenu.getItems().addAll(fm1, fm2, fm3, fm4);

        Menu stepMenu = new Menu("Step");
        MenuItem sm1 = new MenuItem("Step");
        sm1.setOnAction(e -> {
            try {
                this.routefinder.step();
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateMaze();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            } catch (NoRouteFoundException err) {
                statusLabel.setText("Status: " + this.routefinder.getStatus());
                AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                alertBox.showAndWait();
            }
        });
        MenuItem sm2 = new MenuItem("Skip");
        sm2.setOnAction(e -> {
            try {
                boolean done;
                do {
                    done = this.routefinder.step();
                } while (!done);
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.updateMaze();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
            } catch (NoRouteFoundException err) {
                statusLabel.setText("Status: " + this.routefinder.getStatus());
                AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                alertBox.showAndWait();
            }
        });
        stepMenu.getItems().addAll(sm1, sm2);

        MenuBar menuBar = new MenuBar();
        menuBar.getMenus().addAll(fileMenu, stepMenu);


        // Main Scene Layout
        HBox.setMargin(mazegraphics, new Insets(35, 40, 0, 0));
        container.getChildren().addAll(mazegraphics);
        layout.setAlignment(Pos.CENTER);
        layout.getChildren().addAll(topBtns, container);
        scrollPane.setPannable(true);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);
        scrollPane.setContent(layout);
        root.setLeft(legendBarContainer);
        root.setRight(stepBtns);
        root.setCenter(scrollPane);
        root.setTop(menuBar);
        root.setBottom(statusLabel);
        appScene = new Scene(root, 900, 600);
        appScene.getStylesheets().add("./stylesheet.css");


        // Main Menu Layouts 
        VBox menuLayout = new VBox(30);


        // Main Menu Buttons
        Button mainLoadMapBtn = new Button("Load Map");
        mainLoadMapBtn.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Load File");
            fileChooser.setInitialDirectory(Paths.get("./resources/mazes").toFile());
            File file;
            try {
                file = fileChooser.showOpenDialog(stage); 
            } catch (IllegalArgumentException err) {
                fileChooser.setInitialDirectory(Paths.get(".").toFile());
                file = fileChooser.showOpenDialog(stage); 
            }
            if (file != null) {
                try {
                    this.routefinder = new RouteFinder(Maze.fromTxt(file.toString()));
                    this.mazegraphics.setMaze(this.routefinder.toString());
                    this.mazegraphics.setupGraphics();
                    statusLabel.setText(initialStatus);
                    stage.setScene(appScene);
                    this.mazegraphics.updateMaze();
                    noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                } catch (InvalidMazeException err) {
                    AlertBox alertBox = new AlertBox(err.getClass().getName(), err.getMessage());
                    alertBox.showAndWait();
                }
            }
        });
        Button mainLoadRouteBtn = new Button("Load Route");
        mainLoadRouteBtn.setOnAction(e -> {
            FileChooser fileChooser = new FileChooser();
            fileChooser.setTitle("Load File");
            fileChooser.setInitialDirectory(Paths.get(".").toFile());
            File file = fileChooser.showOpenDialog(stage); 
            if (file != null) {
                this.routefinder = RouteFinder.load(file.toString());
                this.mazegraphics.setMaze(this.routefinder.toString());
                this.mazegraphics.setupGraphics();
                noOfSteps.setText("Number of\nSteps: " + this.routefinder.getNoOfSteps());
                statusLabel.setText("Status: \n" + this.routefinder.getStatus());
                stage.setScene(appScene);
                this.mazegraphics.updateMaze();
            }
        });
        Button exitBtn = new Button("Quit");
        exitBtn.setOnAction(e -> {
            stage.close();
        });


        // Menu Scene Layout
        menuLayout.setAlignment(Pos.CENTER);
        menuLayout.getChildren().addAll(mainLabel, mainLoadMapBtn, mainLoadRouteBtn, exitBtn);
        mainMenuScene = new Scene(menuLayout, 400, 400);
        mainMenuScene.getStylesheets().add("./stylesheet.css");


        // Stage Settings
        stage.setScene(mainMenuScene);
        stage.setTitle("Maze Solver");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
