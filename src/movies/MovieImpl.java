package movies;

/**
 * This class implements the movie interface. The movie has a title, director, and year of release.
 */
public class MovieImpl implements Movie {

  private final String title;
  private final Person director;
  private final int year;

  /**
   * Constructs a Movie object and initializes it to the movie's title, director and year.
   *
   * @param title    the title of this movie
   * @param director the name of the movie's director
   * @param year     the year the movie was released
   */
  public MovieImpl(String title, Person director, int year) {
    this.title = title;
    this.director = director;
    this.year = year;
  }

  @Override public String getTitle() {
    return null;
  }

  @Override public Person getDirector() {
    return null;
  }

  @Override public int getYear() {
    return 0;
  }

  @Override public String toString() {
    return null;
  }

  @Override public int compareTo(Movie o) {
    return 0;
  }
}
