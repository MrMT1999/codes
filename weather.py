#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  // Check if the user has specified a directory or file to open.
  if (argc != 2) {
    fprintf(stderr, "Usage: %s <directory/file>\n", argv[0]);
    return EXIT_FAILURE;
  }

  // Open the directory or file.
  int ret = chdir(argv[1]);
  if (ret != 0) {
    perror("chdir");
    return EXIT_FAILURE;
  }

  // Print a success message.
  printf("Opened '%s'\n", argv[1]);

  return EXIT_SUCCESS;
}
