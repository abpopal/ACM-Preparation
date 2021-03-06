package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int t = input.nextInt();
        for (int z = 0; z < t; z++) {
            int steps = 0;
            long x;
            long k = input.nextLong();
            long m = input.nextLong();
            long n = input.nextLong();
            while(k < m){
                if(m % n == 0){
                    m /= n;
                    steps++;
                }else{
                    x = ( n - (m % n));
                    m += ( n - (m % n)) / 2 * 2 + ( n - (m % n)) % 2;
                    steps += x / 2 + x % 2;
                }
            }
            if(k > m){
                steps += (k-m)/2+(k-m)%2;
            }
            System.out.println(steps);
        }
    }
}
