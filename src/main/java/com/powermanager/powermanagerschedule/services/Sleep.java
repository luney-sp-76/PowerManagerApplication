package com.powermanager.powermanagerschedule.services;

public class Sleep {

    public static void sleep(int i) {
        try {
            Thread.sleep(i);
        }catch(InterruptedException interruptedException){
            System.out.println(interruptedException.getMessage());
        }
    }
}