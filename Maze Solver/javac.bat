@del /s /q *.class

"C:\Program Files\AdoptOpenJDK\jdk-14.0.1.7-hotspot\bin\javac.exe" -d ./bin --module-path ./lib/ --add-modules=javafx.controls,javafx.fxml --source-path ./src ./src/*.java %1
