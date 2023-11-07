#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dirent.h>
#include <string.h>

int main(int argc, char **argv) {
  // Check if the user provided a filename to search for.
  if (argc != 2) {
    printf("Usage: findfile <filename>\n");
    exit(1);
  }

  // Get the current working directory.
  char cwd[1024];
  getcwd(cwd, sizeof(cwd));

  // Open the current working directory.
  DIR *dir = opendir(cwd);
  if (dir == NULL) {
    perror("opendir");
    exit(1);
  }

  // Create a buffer to store the full path of the file we are searching for.
  char filepath[1024];
  snprintf(filepath, sizeof(filepath), "%s/%s", cwd, argv[1]);

  // Iterate over all of the entries in the current working directory.
  struct dirent *entry;
  while ((entry = readdir(dir)) != NULL) {
    // If the entry is a directory, recursively search it.
    if (entry->d_type == DT_DIR) {
      if (strcmp(entry->d_name, ".") != 0 && strcmp(entry->d_name, "..") != 0) {
        chdir(entry->d_name);
        findfile(argv[1]);
        chdir("..");
      }
    } else {
      // If the entry is a file, check if it matches the filename we are searching for.
      if (strcmp(entry->d_name, argv[1]) == 0) {
        // If the entry matches the filename, print its full path.
        printf("%s\n", filepath);
      }
    }
  }

  // Close the current working directory.
  closedir(dir);

  return 0;
}
