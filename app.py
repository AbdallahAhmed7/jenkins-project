from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CYBER CLOCK</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            background-color: #050510;
            color: #00f5ff;
            font-family: 'Share Tech Mono', monospace;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        /* Animated grid background */
        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-image:
                linear-gradient(rgba(0,245,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,245,255,0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: gridMove 20s linear infinite;
            z-index: 0;
        }

        /* Scanlines overlay */
        body::after {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: repeating-linear-gradient(
                0deg,
                transparent,
                transparent 2px,
                rgba(0,0,0,0.15) 2px,
                rgba(0,0,0,0.15) 4px
            );
            pointer-events: none;
            z-index: 10;
        }

        @keyframes gridMove {
            0%   { transform: translateY(0); }
            100% { transform: translateY(50px); }
        }

        .container {
            position: relative;
            z-index: 5;
            text-align: center;
            padding: 50px 60px;
            border: 1px solid rgba(0,245,255,0.2);
            background: rgba(0,5,20,0.8);
            box-shadow:
                0 0 40px rgba(0,245,255,0.1),
                inset 0 0 40px rgba(0,245,255,0.03);
        }

        /* Corner decorations */
        .container::before,
        .container::after {
            content: '';
            position: absolute;
            width: 20px; height: 20px;
        }
        .container::before {
            top: -1px; left: -1px;
            border-top: 2px solid #00f5ff;
            border-left: 2px solid #00f5ff;
            box-shadow: -4px -4px 10px rgba(0,245,255,0.5);
        }
        .container::after {
            bottom: -1px; right: -1px;
            border-bottom: 2px solid #bf00ff;
            border-right: 2px solid #bf00ff;
            box-shadow: 4px 4px 10px rgba(191,0,255,0.5);
        }

        .label {
            font-size: 11px;
            letter-spacing: 8px;
            color: rgba(0,245,255,0.5);
            text-transform: uppercase;
            margin-bottom: 30px;
        }

        .clock {
            font-family: 'Orbitron', monospace;
            font-size: clamp(52px, 10vw, 90px);
            font-weight: 900;
            letter-spacing: 6px;
            color: #ffffff;
            text-shadow:
                0 0 10px #00f5ff,
                0 0 30px #00f5ff,
                0 0 60px rgba(0,245,255,0.5);
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { text-shadow: 0 0 10px #00f5ff, 0 0 30px #00f5ff, 0 0 60px rgba(0,245,255,0.5); }
            50%       { text-shadow: 0 0 20px #00f5ff, 0 0 50px #00f5ff, 0 0 100px rgba(0,245,255,0.8); }
        }

        .separator { color: #bf00ff; animation: blink 1s step-end infinite; }
        @keyframes blink { 50% { opacity: 0; } }

        .divider {
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, transparent, #00f5ff, #bf00ff, transparent);
            margin: 24px 0;
        }

        .date {
            font-family: 'Orbitron', monospace;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 4px;
            color: #bf00ff;
            text-shadow: 0 0 10px #bf00ff, 0 0 20px rgba(191,0,255,0.5);
        }

        .timezone {
            font-size: 11px;
            letter-spacing: 4px;
            color: rgba(0,245,255,0.35);
            margin-top: 14px;
        }

        .badge {
            margin-top: 36px;
            font-size: 10px;
            letter-spacing: 3px;
            color: rgba(255,255,255,0.15);
            text-transform: uppercase;
        }

        .badge span {
            color: rgba(0,245,255,0.3);
        }

        /* Floating corner text */
        .corner-text {
            position: fixed;
            font-size: 10px;
            letter-spacing: 2px;
            color: rgba(0,245,255,0.2);
            z-index: 5;
        }
        .corner-text.tl { top: 20px; left: 20px; }
        .corner-text.tr { top: 20px; right: 20px; }
        .corner-text.bl { bottom: 20px; left: 20px; }
        .corner-text.br { bottom: 20px; right: 20px; }
        .footer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(0,245,255,0.1);
            font-size: 11px;
            letter-spacing: 3px;
            color: rgba(255,255,255,0.2);
            text-transform: uppercase;
        }

        .footer strong {
            display: block;
            margin-top: 6px;
            font-size: 13px;
            letter-spacing: 4px;
            color: rgba(0,245,255,0.5);
        }

        .links {
            margin-top: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
        }

        .links a {
            color: #bf00ff;
            text-decoration: none;
            letter-spacing: 2px;
            font-size: 11px;
            transition: all 0.3s ease;
            text-shadow: 0 0 8px rgba(191,0,255,0.5);
        }

        .links a:hover {
            color: #00f5ff;
            text-shadow: 0 0 12px rgba(0,245,255,0.8);
        }

        .dot { color: rgba(255,255,255,0.15); }
    </style>
</head>
<body>

    <div class="corner-text tl">SYS::ONLINE</div>
    <div class="corner-text tr">v1.0.0</div>
    <div class="corner-text bl">JENKINS CI/CD</div>
    <div class="corner-text br">DOCKER::ACTIVE</div>

    <div class="container">
        <div class="label">// system time //</div>

        <div class="clock">
            <span id="hh">00</span>
            <span class="separator">:</span>
            <span id="mm">00</span>
            <span class="separator">:</span>
            <span id="ss">00</span>
        </div>

        <div class="divider"></div>

        <div class="date" id="date">LOADING...</div>
        <div class="timezone" id="tz"></div>

        <div class="badge">deployed via <span>jenkins pipeline</span></div>
        
        <div class="footer">
            <span>developed by</span>
            <strong>Abdallah Ahmed</strong>
            <div class="links">
                <a href="https://github.com/AbdallahAhmed7" target="_blank">⌥ GitHub</a>
                <span class="dot">·</span>
                <a href="https://www.linkedin.com/in/abdallahahmed7/" target="_blank">⌘ LinkedIn</a>
            </div>
         </div>

    </div>



    <script>
        const DAYS   = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'];
        const MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'];

        function pad(n) { return String(n).padStart(2, '0'); }

        function tick() {
            const now = new Date();
            document.getElementById('hh').textContent   = pad(now.getHours());
            document.getElementById('mm').textContent   = pad(now.getMinutes());
            document.getElementById('ss').textContent   = pad(now.getSeconds());
            document.getElementById('date').textContent =
                DAYS[now.getDay()] + ' · ' +
                pad(now.getDate()) + ' ' +
                MONTHS[now.getMonth()] + ' ' +
                now.getFullYear();
            document.getElementById('tz').textContent =
                Intl.DateTimeFormat().resolvedOptions().timeZone.toUpperCase();
        }

        tick();
        setInterval(tick, 1000);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
