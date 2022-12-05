package com.powermanager.powermanagerschedule.plugmodel;

import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class PlugState {
    private String entityID;
    private String state;
    private Attributes attributes;
    private String lastChanged;
    private String lastUpdated;
    private Context context;

}