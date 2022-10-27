//
//  BatteryView.swift
//  PowerManagerApp
//
//  Created by Paul Olphert on 27/10/2022.
//

import SwiftUI

struct ContentView: View {
    @State private var progress = 0.0
    
    
    var body: some View {
        ZStack{
            Color.black.opacity(0.9)
                .ignoresSafeArea()
            VStack{
                BatteryView(progress: $progress, fill: .green, outline: .white)
                Slider(value: $progress, in : 0...1.0)
                    .tint(.green)
                    .padding()
                VStack(alignment: .trailing){
                    Text("Set lowest %")
                        .font(.caption)
                        .foregroundColor(.white)
                }
            }
        }
        .onAppear {
            withAnimation(.interpolatingSpring(stiffness: 20.0, damping: 8.0)){
                self.progress = 0.7
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
