//
//  PowerManagerAppApp.swift
//  PowerManagerApp
//
//  Created by Paul Olphert on 13/10/2022.
//

import SwiftUI

@main
struct PowerManagerAppApp: App {
    var body: some Scene {
        WindowGroup {
            BatteryView(progress: .constant(0.7), fill: .green, outline: .black)
        }
    }
}
