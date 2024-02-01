import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import movies.Movie;
import movies.MovieImpl;
import movies.Person;

/**
 * Read movies from a CSV file, convert them into Movie objects, and then add them to a LinkedList.
 */
public class Main {

  /**
   * The logger for this class. A logger is used to log messages to a log file.
   */
  private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

  /**
   * Driver class. Read movies from a CSV file, convert them into Movie objects, and then add them
   * to a LinkedList. The list is order chronologically.
   *
   * @param args command line arguments (unused)
   */
  public static void main(String[] args) {
    // Movie info
    String filePath = "res/movies_data.csv";
    String movieString;
    boolean isFirstLine = true;

    // Create a LinkedList to store Movie objects.
    List<Movie> movieList = new LinkedList<>();

    // Read the CSV file line by line; skip the first line (header).
    try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
      while ((movieString = br.readLine()) != null) {
        if (isFirstLine) {
          isFirstLine = false; // Skip the first line (header)
          continue;
        }
        // Turn Movie String into Movie object and add to the LinkedList in the right location.
        insertInOrder(turnStringIntoMovie(movieString), movieList);
      }
    } catch (IOException e) {
      LOGGER.log(Level.SEVERE, "Error reading file " + filePath, e);
    }

    // Print the list of movies.
    System.out.println("List of movies:");
    for (Movie movie : movieList) {
      System.out.println(movie.toString());
    }

    // Print the list of movies made in 1994
    System.out.println("\nList of movies made in 1994:");
    movieList.stream()
        .filter(movie -> movie.getYear() == 1994)
        .forEach(System.out::println);
  }

  /**
   * Convert a line of text from the Movie CSV file into a Movie object.
   *
   * @param movieString a line of text from the Movie CSV file
   * @return a Movie object
   */
  private static Movie turnStringIntoMovie(String movieString) {
    // Movie info
    String[] movieInfoArray = movieString.split(",");

    // Director Info
    String[] directorInfoArray = movieInfoArray[1].split(" ");
    String firstName = directorInfoArray[0];
    StringBuilder lastName = new StringBuilder();
    for (int index = 1; index < directorInfoArray.length; index++) {
      if (index > 1) {
        lastName.append(" "); // For directors with more than one word in their last name
      }
      lastName.append(directorInfoArray[index]);
    }

    // Year Info
    int year = Integer.parseInt(movieInfoArray[2]);

    return new MovieImpl(movieInfoArray[0], new Person(firstName, lastName.toString()), year);
  }

  /**
   * Insert a Movie object into a list of Movie objects in chronological order.
   *
   * @param movie     a Movie object
   * @param movieList a list of Movie objects
   */
  private static void insertInOrder(Movie movie, List<Movie> movieList) {
    for (int index = 0; index < movieList.size(); index++) {
      if (movie.compareTo(movieList.get(index)) < 0) {
        movieList.add(index, movie);
        return; // Return after inserting the movie in the correct position
      }
    }
    // If the movie wasn't inserted in the loop, it means it should be placed at the end of the list
    movieList.add(movie);
  }
}
