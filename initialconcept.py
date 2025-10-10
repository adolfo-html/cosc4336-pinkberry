import sys
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QTextEdit, QLabel)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette
import random

class LCARSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("LCARS Interface")
        self.setGeometry(100, 100, 1200, 800)
        
        # Set main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create button panel (10% of width)
        self.button_panel = QWidget()
        self.button_panel.setFixedWidth(int(self.width() * 0.1))
        button_layout = QVBoxLayout(self.button_panel)
        button_layout.setSpacing(10)
        button_layout.setContentsMargins(5, 5, 5, 5)
        
        # Add LCARS-style buttons with rounded corners using stylesheets
        button_data = [
            ("SYSTEM STATUS", "#FF9900", self.show_system_status),
            ("PROCESSES", "#3366CC", self.show_processes),
            ("SERVICES", "#9966CC", self.show_services),
            ("NETWORK", "#CC6699", self.show_network),
            ("DISK INFO", "#66CC99", self.show_disk_info),
            ("EXECUTE", "#FF6666", self.execute_custom),
            ("CLEAR", "#6666FF", self.clear_display)
        ]
        
        self.buttons = []
        for text, color, handler in button_data:
            btn = QPushButton(text)
            btn.setFixedHeight(60)
            btn.setFont(QFont("Arial", 12, QFont.Bold))
            # Use stylesheet for rounded corners instead of custom paintEvent
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: black;
                    border: none;
                    border-radius: 15px;
                    font-weight: bold;
                }}
                QPushButton:pressed {{
                    background-color: #FFCC00;
                }}
            """)
            btn.clicked.connect(handler)
            self.buttons.append(btn)
            button_layout.addWidget(btn)
        
        button_layout.addStretch()
        main_layout.addWidget(self.button_panel)
        
        # Create content area (90% of width)
        content_panel = QWidget()
        content_layout = QVBoxLayout(content_panel)
        content_layout.setContentsMargins(10, 10, 10, 10)
        
        # Header
        header = QLabel("LCARS COMPUTER INTERFACE")
        header.setStyleSheet("""
            QLabel {
                background-color: #FF9900;
                color: white;
                font-family: "Arial";
                font-size: 24px;
                font-weight: bold;
                padding: 10px;
                qproperty-alignment: AlignCenter;
                border-radius: 10px;
            }
        """)
        header.setFixedHeight(60)
        content_layout.addWidget(header)
        
        # Text display area
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        palette = self.text_display.palette()
        palette.setColor(QPalette.Base, QColor("#000000"))
        palette.setColor(QPalette.Text, QColor("#FFCC00"))
        self.text_display.setPalette(palette)
        
        self.text_display.setStyleSheet("""
            QTextEdit {
                font-family: "Courier New";
                font-size: 14px;
                border: 2px solid #FF9900;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        content_layout.addWidget(self.text_display)
        
        # Status bar
        self.status = QLabel("System Ready")
        self.status.setStyleSheet("""
            QLabel {
                background-color: #3366CC;
                color: white;
                font-family: "Arial";
                font-size: 14px;
                padding: 5px;
                border-radius: 5px;
            }
        """)
        self.status.setFixedHeight(30)
        content_layout.addWidget(self.status)
        
        main_layout.addWidget(content_panel)
        
        # Set initial text
        self.text_display.append("LCARS System Initialized")
        self.text_display.append("Type: Main Computer Interface")
        self.text_display.append("Status: All Systems Operational")
        self.text_display.append("Ready to Receive Commands\n")
        
        # Set up animation timer
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate_text)
        self.animation_timer.start(3000000)  # Add text every 3 seconds
        
        # Initialize animation text pool
        self.animation_texts = [
            "Running system diagnostics...",
            "Monitoring network traffic...",
            "Checking subspace communications...",
            "Analyzing sensor data...",
            "Updating stellar cartography...",
            "Compiling mission logs...",
            "Verifying shield integrity...",
            "Optimizing warp field parameters..."
        ]
        
    def play_sound(self):
        # Play a system beep sound
        QApplication.beep()
        
    def animate_text(self):
        # Add random system messages to simulate a working system
        text = random.choice(self.animation_texts)
        self.text_display.append(text)
        # Scroll to bottom
        self.text_display.verticalScrollBar().setValue(
            self.text_display.verticalScrollBar().maximum()
        )
        
    def execute_powershell(self, command):
        self.play_sound()
        self.status.setText(f"Executing: {command}")
        
        try:
            # Execute PowerShell command
            result = subprocess.run(
                ["powershell", "-Command", command],
                capture_output=True, 
                text=True, 
                timeout=30
            )
            
            if result.returncode == 0:
                self.text_display.append(f"\n> {command}")
                self.text_display.append(result.stdout)
                self.status.setText("Command executed successfully")
            else:
                self.text_display.append(f"\n> Error executing: {command}")
                self.text_display.append(result.stderr)
                self.status.setText("Command failed")
                
        except subprocess.TimeoutExpired:
            self.text_display.append(f"\n> Command timed out: {command}")
            self.status.setText("Command timed out")
        except Exception as e:
            self.text_display.append(f"\n> Exception: {str(e)}")
            self.status.setText("Exception occurred")
            
        # Scroll to bottom
        self.text_display.verticalScrollBar().setValue(
            self.text_display.verticalScrollBar().maximum()
        )
        
    def show_system_status(self):
        self.execute_powershell("ls")
        
    def show_processes(self):
        self.execute_powershell("Get-NetIPAddress")
        
    def show_services(self):
        self.execute_powershell("gps")
        
    def show_network(self):
        self.execute_powershell("ls")
        
    def show_disk_info(self):
        self.execute_powershell("ls")
        
    def execute_custom(self):
        self.text_display.append("\n> Custom command execution not implemented")
        self.text_display.append("This would open a dialog for custom commands")
        self.status.setText("Custom command feature not implemented")
        
    def clear_display(self):
        self.play_sound()
        self.text_display.clear()
        self.text_display.append("LCARS Display Cleared")
        self.text_display.append("System Ready for Commands\n")
        self.status.setText("Display cleared")
        
    def resizeEvent(self, event):
        # Maintain button panel at 10% of window width
        new_width = int(self.width() * 0.1)
        self.button_panel.setFixedWidth(new_width)
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle("Fusion")
    
    window = LCARSWindow()
    window.show()
    
    sys.exit(app.exec_())