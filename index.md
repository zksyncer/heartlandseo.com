<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heartland SEO - Local SEO Services for Missouri and Kansas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        .header {
            background: linear-gradient(to right, #0066cc, #00cc66);
            color: white;
            padding: 20px;
            text-align: center;
        }
        .content {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px 5px;
            background-color: #007bff;
            color: white;
            text-align: center;
            text-decoration: none;
            border-radius: 5px;
        }
        .services, .why-choose-us {
            margin-top: 20px;
        }
        .counter {
            text-align: center;
            margin-top: 20px;
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Heartland SEO</h1>
        <p>Local SEO Services for Missouri and Kansas Businesses</p>
    </div>
    
    <div class="content">
        <h2>Welcome to Heartland SEO</h2>
        <p>Boost your local business visibility with our expert SEO services tailored for Missouri and Kansas.</p>
        
        <div class="services">
            <h3>Our Services</h3>
            <ul>
                <li>Google Business Profile Optimization</li>
                <li>Local SEO Strategy</li>
                <li>Content Creation for Local Markets</li>
                <li>Citation Building and Management</li>
            </ul>
        </div>
        
        <div class="why-choose-us">
            <h3>Why Choose Heartland SEO?</h3>
            <ol>
                <li>Local Expertise: We know Missouri and Kansas markets inside out</li>
                <li>Proven Results: Increased visibility for 100+ local businesses</li>
                <li>Tailored Strategies: Custom approach for each city and business type</li>
            </ol>
        </div>
        
        <a href="packages.html" class="btn">View Our Packages</a>
        <a href="mailto:info@heartlandseo.com" class="btn">Contact Us</a>
        <a href="cities.html" class="btn">Find Your City</a>
        
        <div class="counter">
            Page Views: <span id="count">1</span>
        </div>
    </div>

    <script>
        let count = localStorage.getItem('pageViews') || 0;
        count++;
        document.getElementById('count').textContent = count;
        localStorage.setItem('pageViews', count);
    </script>
</body>
</html>
