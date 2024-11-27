from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.properties import NumericProperty
import requests
import json
from datetime import datetime
from functools import partial

class MentalWellnessMonitor(BoxLayout):
    stress_level = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Initialize data storage
        self.hr_data = []
        self.spo2_data = []
        self.gsr_data = []
        self.temp_data = []
        
        self._create_ui()
        self._schedule_updates()
    
    def _create_ui(self):
        # Title
        title = Label(
            text='Mental Wellness Monitor',
            size_hint_y=0.1,
            font_size='24sp'
        )
        self.add_widget(title)
        
        # Vital Signs Section
        vitals_layout = BoxLayout(orientation='horizontal', size_hint_y=0.3)
        
        # Heart Rate
        self.hr_label = Label(
            text='Heart Rate\n-- BPM',
            halign='center',
            markup=True
        )
        vitals_layout.add_widget(self.hr_label)
        
        # SpO2
        self.spo2_label = Label(
            text='SpO2\n--%',
            halign='center',
            markup=True
        )
        vitals_layout.add_widget(self.spo2_label)
        
        # Temperature
        self.temp_label = Label(
            text='Temperature\n--°C',
            halign='center',
            markup=True
        )
        vitals_layout.add_widget(self.temp_label)
        
        # GSR
        self.gsr_label = Label(
            text='Stress Level\n--',
            halign='center',
            markup=True
        )
        vitals_layout.add_widget(self.gsr_label)
        
        self.add_widget(vitals_layout)
        
        # Graphs Section
        graphs_layout = BoxLayout(orientation='vertical', size_hint_y=0.4)
        
        # Heart Rate Graph
        self.hr_graph = Graph(
            xlabel='Time',
            ylabel='BPM',
            x_ticks_minor=5,
            x_ticks_major=25,
            y_ticks_major=50,
            y_grid_label=True,
            x_grid_label=True,
            padding=5,
            x_grid=True,
            y_grid=True,
            xmin=0,
            xmax=100,
            ymin=40,
            ymax=200
        )
        self.hr_plot = MeshLinePlot(color=[1, 0, 0, 1])
        self.hr_plot.points = [(0, 0)]  # Initialize with a point to avoid errors
        self.hr_graph.add_plot(self.hr_plot)
        graphs_layout.add_widget(self.hr_graph)
        
        self.add_widget(graphs_layout)
        
        # Stress Level Indicator
        stress_layout = BoxLayout(orientation='vertical', size_hint_y=0.2)
        stress_label = Label(
            text='Current Stress Level',
            size_hint_y=0.3
        )
        stress_layout.add_widget(stress_label)
        
        self.stress_bar = ProgressBar(
            max=100,
            value=0,
            size_hint_y=0.7
        )
        stress_layout.add_widget(self.stress_bar)
        
        self.add_widget(stress_layout)
        
        # Recommendations Section
        self.recommendation_label = Label(
            text='Wellness Recommendations will appear here',
            size_hint_y=0.1,
            markup=True
        )
        self.add_widget(self.recommendation_label)
        
        # Emergency Button
        self.emergency_button = Button(
            text='Contact Mental Health Professional',
            size_hint_y=0.1,
            background_color=[1, 0, 0, 1]
        )
        self.emergency_button.bind(on_press=self.show_emergency_popup)
        self.add_widget(self.emergency_button)
    
    def _schedule_updates(self):
        # Update every 15 seconds to match ThingSpeak delay
        Clock.schedule_interval(self.update_data, 15)
    
    def update_data(self, dt):
        # Fetch data from ThingSpeak
        try:
            url = "https://api.thingspeak.com/channels/2702924/feeds.json?api_key=ME07ZYF3SA50HGDS&results=1"
            response = requests.get(url)
            data = response.json()
            
            if data['feeds']:
                latest = data['feeds'][-1]
                
                # Update labels with color coding
                hr_val = float(latest["field2"])
                self.hr_label.text = f'Heart Rate\n[color={"ff0000" if hr_val > 100 else "00ff00"}]{hr_val}[/color] BPM'
                
                spo2_val = float(latest["field4"])
                self.spo2_label.text = f'SpO2\n[color={"ff0000" if spo2_val < 95 else "00ff00"}]{spo2_val}[/color]%'
                
                temp_val = float(latest["field1"])
                self.temp_label.text = f'Temperature\n[color={"ff0000" if temp_val > 37.5 else "00ff00"}]{temp_val}[/color]°C'
                
                gsr_val = float(latest["field3"])
                self.gsr_label.text = f'GSR\n[color={"ff0000" if gsr_val > 3000 else "00ff00"}]{gsr_val}[/color]'
                
                # Update graph
                self.hr_data.append(hr_val)
                if len(self.hr_data) > 100:
                    self.hr_data.pop(0)
                self.hr_plot.points = [(i, x) for i, x in enumerate(self.hr_data)]
                
                # Calculate stress level based on GSR and HR
                self.stress_level = min(100, max(0, (gsr_val/4096 * 100 + (hr_val-60)/140 * 100) / 2))
                self.stress_bar.value = self.stress_level
                
                # Update recommendations
                self._update_recommendations()
                
        except Exception as e:
            print(f"Error updating data: {e}")
    
    def _update_recommendations(self):
        if self.stress_level > 75:
            self.recommendation_label.text = "[color=ff0000]High stress detected![/color]\nTry deep breathing exercises or take a short walk."
        elif self.stress_level > 50:
            self.recommendation_label.text = "[color=ffa500]Moderate stress.[/color]\nConsider taking a break or practicing mindfulness."
        elif self.stress_level > 25:
            self.recommendation_label.text = "[color=ffff00]Slight stress elevation.[/color]\nStay hydrated and maintain regular breaks."
        else:
            self.recommendation_label.text = "[color=00ff00]Stress levels normal.[/color]\nKeep up the good work!"
    
    def show_emergency_popup(self, instance):
        content = BoxLayout(orientation='vertical', padding=10)
        content.add_widget(Label(
            text='Emergency Contact Information:\n\nMental Health Hotline: 9152987821',
            halign='center'
        ))
        button = Button(text='Close', size_hint_y=0.3)
        content.add_widget(button)
        
        popup = Popup(
            title='Emergency Contacts',
            content=content,
            size_hint=(0.8, 0.8)
        )
        button.bind(on_press=popup.dismiss)
        popup.open()

class MentalWellnessApp(App):
    def build(self):
        return MentalWellnessMonitor()

if __name__ == '__main__':
    MentalWellnessApp().run()
