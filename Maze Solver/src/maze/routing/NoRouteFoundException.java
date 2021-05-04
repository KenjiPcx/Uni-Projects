package maze.routing;

/**
 * This exception is thrown when a route cannot be found
 * for a maze.
 */
public class NoRouteFoundException extends RuntimeException {
    NoRouteFoundException(String errorMsg){
        super(errorMsg);
    }
}
