//
//  ContentView.swift
//  PowerManagerApp
//
//  Created by Paul Olphert on 13/10/2022.
//

import SwiftUI

struct ControlPanelView: View {
    var body: some View {
        VStack {
            Image(systemName: "globe")
                .imageScale(.large)
                .foregroundColor(.accentColor)
            Text("Hello, world!")
            Text("Power To Behold")
        }
        .padding()
    }
}

struct ControlPanelView_Previews: PreviewProvider {
    static var previews: some View {
        ControlPanelView()
    }
}
