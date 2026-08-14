from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("""
    <html>
        <head>
            <title>🏥 Hospital Management System</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f8ff; }
                h1 { color: #2c3e50; font-size: 3em; }
                .container { max-width: 800px; margin: 0 auto; }
                .feature { display: inline-block; margin: 10px; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
                a { color: #3498db; text-decoration: none; }
                .btn { display: inline-block; padding: 10px 20px; margin: 10px; background: #3498db; color: white; border-radius: 5px; }
                .btn:hover { background: #2980b9; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🏥 Hospital Management System</h1>
                <p style="font-size: 1.2em; color: #555;">Comprehensive Healthcare Management Platform</p>
                
                <div>
                    <div class="feature">👨‍⚕️ Patient Management</div>
                    <div class="feature">📅 Appointments</div>
                    <div class="feature">💊 Pharmacy</div>
                    <div class="feature">💰 Billing</div>
                    <div class="feature">📋 Medical Records</div>
                    <div class="feature">📊 Analytics</div>
                </div>
                
                <div style="margin-top: 30px;">
                    <a href="/admin/" class="btn">Admin Panel</a>
                    <a href="/api/docs/" class="btn">API Documentation</a>
                    <a href="https://github.com/charllote122/hospital-management" class="btn" style="background: #2c3e50;">GitHub</a>
                </div>
                
                <p style="margin-top: 40px; color: #888;">
                    🚀 Deployed on Render | Django 4.2.11 | PostgreSQL
                </p>
            </div>
        </body>
    </html>
    """)
