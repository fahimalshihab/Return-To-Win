
#define BUFSIZE 32
#define FLAGSIZE 64

void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  fgets(buf,FLAGSIZE,f);
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}


int main(){
  puts("Please enter your string: ");
  vuln();
  return 0;
}

