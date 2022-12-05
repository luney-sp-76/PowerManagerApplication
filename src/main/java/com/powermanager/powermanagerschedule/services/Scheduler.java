package com.powermanager.powermanagerschedule.services;

import lombok.Value;

import java.io.IOException;
import java.lang.reflect.Type;

import static java.lang.Thread.sleep;

public class Scheduler {

    private String url_plug_state = ("${url_plug_state}");
    String url_plug_turn_on = ("${url_plug_turn_on}");//curl works, python works, java works
    String url_plug_turn_off = ("${url_plug_turn_off}");//curl works, python works, java works
    String url_plug_toggle = ("${url_plug_toggle}");
    String url_iphone_battery_state = ("${url_iphone_battery_state}");//working
    String url_iphone_battery_level = ("${url_iphone_battery_level}");//working

    @Value("${authorization}")
    private String bearer;


    CallApi callApi = new CallApi();
    Sleep sleep = new Sleep();

    //assign the battery level as a String
    String batteryLevel = callApi.getState(url_iphone_battery_level, bearer);
    //get the charging state
    String batteryState = callApi.getState(url_iphone_battery_state, bearer);
    //get the plug current state
    String plugCurrentState = callApi.getState(url_plug_state, bearer);
        try {
        sleep(20000);
    }catch(InterruptedException e){
        System.out.println(e.getMessage());
    }
        callApi.changeState(url_plug_turn_on, bearer);
        try {
        sleep(20000);
    }catch(InterruptedException f){
        System.out.println(f.getMessage());
    }
    PlugState plugState = (PlugState) createPlugObject(plugCurrentState);
        System.out.println("The plug is " + plugState.getState());
    checkChargeAndState(batteryLevel, 82, batteryState, plugCurrentState, url_plug_turn_on, url_plug_turn_off, url_plug_toggle, bearer, callApi);

}



    /**
     * @param response2
     * @return
     */
    private static Object createIphoneObject(String response2) {
        Gson gson = new Gson();
        IPhoneBatteryState batteryState = gson.fromJson(response2, (Type) IPhoneBatteryState.class);
        return batteryState;
    }

    /**
     * @param response2
     * @return
     */
    private static Object createPlugObject(String response2) {
        Gson gson = new Gson();
        PlugState plugState = gson.fromJson(response2, (Type) PlugState.class);
        //System.out.println(batteryState.getState());
        return plugState;
    }





    public static void checkChargeAndState(String batteryLevel, int desiredLevel, String batteryState, String plugCurrentState, String url_plug_turn_off, String url_plug_turn_on, String url_plug_toggle, String bearer, CallApi callApi) throws IOException {
        boolean flag = true;
        final String ISNOTCHARGING = "Not Charging";
        final String ISCHARGING = "Charging";
        final String FULL = "Full";
        IPhoneBatteryState batteryPercentage = (IPhoneBatteryState) createIphoneObject(batteryLevel);
        // change the battery level to an int
        int batteryPercentageLevel = Integer.parseInt(batteryPercentage.getState());
        System.out.println("The battery Percentage level " + batteryPercentageLevel);

        IPhoneBatteryState batteryChargeLevel = (IPhoneBatteryState) createIphoneObject(batteryState);
        PlugState plugState = (PlugState) createPlugObject(plugCurrentState);

        System.out.println("Below the desired Level " + (batteryPercentageLevel < desiredLevel));//the battery level is lower than the  desired percentage
        System.out.println("The desired Level is: " + desiredLevel);
        System.out.println("The Phone is Charging " + (batteryChargeLevel.getState().equals(ISCHARGING)));
        //and the phone is charging
        System.out.println("2: " + batteryChargeLevel.getState());
        System.out.println("Over or at the charge level " + (batteryPercentageLevel >= desiredLevel));//it's the same or greater and the phone is charging
        System.out.println("The plug is on is: " + (plugState.getState().equals("on")));
        System.out.println("Not charging and the plug is on " + (batteryChargeLevel.getState().equals(ISNOTCHARGING) && plugState.getState().equals("on")));//the phone is not charging and the plug is on
        System.out.println();
        System.out.println("The desired battery level = " + desiredLevel + "%");
        System.out.println("The current battery level = " + batteryPercentage.getState() + "%");
        System.out.println("The battery is \"" + batteryChargeLevel.getState() + "\"");
        System.out.println("The plug is " + plugState.getState());
        callApi.changeState(url_plug_toggle, bearer);
        try {
            sleep(20000);
        }catch(InterruptedException g){
            System.out.println(g.getMessage());
        }


////        if (batteryPercentageLevel < desiredLevel && batteryChargeLevel.getState().equals(ISNOTCHARGING)) {
////            //changeState(url_plug_turn_on,  bearer);
////            System.out.println("It's A " + plugState.getState());}
//
//        if (batteryPercentageLevel >= desiredLevel && batteryChargeLevel.getState().equals(ISCHARGING) || batteryPercentageLevel >= desiredLevel && batteryChargeLevel.getState().equals(FULL)) {
//            changeState(url_plug_turn_off, bearer);
//            System.out.println("It's B " + plugState.getState());
//        }
//        if (batteryPercentageLevel < desiredLevel) {
//            changeState(url_plug_turn_on, bearer);
//            System.out.println("It's C " + plugState.getState());
//        }

        System.out.println("The plug is " + plugState.getState());
    }


}



}
