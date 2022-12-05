package com.powermanager.powermanagerschedule.phonemodel;


import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Getter
@NoArgsConstructor
public class IPhoneBatteryState implements getLastUpdated {
    private String entityID;
    private String state;
    private Attributes attributes;
    private String lastChanged;
    private String lastUpdated;
    private Context context;

    @Override
    public String getLastUpdated(){
        String lastUpdated = this.lastUpdated.toString();
        lastUpdated = String.valueOf(LocalDateTime.parse(lastUpdated, DateTimeFormatter.ofPattern("yyyy-MM-dd")));
        return lastUpdated;
    }

    @Override
    public String getLastChanged(){
        String lastChanged = this.lastChanged.toString();
        lastChanged = String.valueOf(LocalDateTime.parse(lastChanged, DateTimeFormatter.ofPattern("yyyy-MM-dd")));
        return lastChanged;
    }

}

