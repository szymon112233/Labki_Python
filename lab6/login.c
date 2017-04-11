
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  char haslo[8];
  char zalogowany;
  zalogowany = 'n';
  strncpy( haslo, argv[1], 8);
  if( strcmp( haslo, "tajne" ) == 0 ){
    zalogowany = 't';
  }
  if( zalogowany == 't' ){
    printf("Poprawne haslo, witamy :)\n");
  } else {
    printf("Bledne haslo, uciekaj :(\n");
  }
  return 0;
} 
