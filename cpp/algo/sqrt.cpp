short sqrt(short num) {
    short op = num;
    short res = 0;
    short one = 1 << 14; // The second-to-top bit is set: 1L<<30 for long

    // "one" starts at the highest power of four <= the argument.
    while (one > op)
        one >>= 2;

    while (one != 0) {
        if (op >= res + one) {
            op -= res + one;
            res = (res >> 1) + one;
        }
        else
          res >>= 1;
        one >>= 2;
    }
    return res;
}

int main(int argc, char *argv){
    short x = sqrt((int)argv[1]);
    printf("%d\n", x);
}
