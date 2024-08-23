<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heartland SEO - Expert SEO Consulting</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js" defer></script>
</head>
<body class="bg-gray-900 text-white">
    <header class="bg-yellow-500 py-4">
        <div class="container mx-auto flex justify-between items-center px-4">
            <h1 class="text-2xl font-bold">Heartland SEO</h1>
            <nav>
                <a href="#" class="mx-2 hover:underline">Home</a>
                <a href="#" class="mx-2 hover:underline">Services</a>
                <a href="#" class="mx-2 hover:underline">About</a>
                <a href="#" class="mx-2 hover:underline">Contact</a>
            </nav>
        </div>
    </header>

    <main class="container mx-auto px-4 py-8">
        <section class="text-center">
            <h2 class="text-4xl font-bold mb-4">Free Download: Get Your First 1000 Email Subscribers</h2>
            <p class="text-xl mb-8">Your blueprint for rapidly growing your list - even if you've struggled in the past!</p>
            <a href="#" class="bg-green-500 text-white font-bold py-2 px-4 rounded-full text-lg hover:bg-green-600 transition duration-300">DOWNLOAD NOW</a>
            <p class="mt-4 text-sm">We guarantee 100% privacy. Your information will not be shared.</p>
        </section>

        <section class="mt-16" x-data="{ timeLeft: 3600 }" x-init="setInterval(() => timeLeft--, 1000)">
            <div class="text-center">
                <h3 class="text-2xl font-bold mb-4">Limited Time Offer</h3>
                <div class="text-4xl font-bold">
                    <span x-text="Math.floor(timeLeft / 3600)"></span>:
                    <span x-text="Math.floor((timeLeft % 3600) / 60)"></span>:
                    <span x-text="timeLeft % 60"></span>
                </div>
            </div>
        </section>

        <section class="mt-16">
            <h3 class="text-2xl font-bold text-center mb-8">Featured In</h3>
            <div class="flex justify-around items-center">
                <img src="path_to_forbes_logo.png" alt="Forbes" class="h-12 opacity-50">
                <img src="path_to_entrepreneur_logo.png" alt="Entrepreneur" class="h-12 opacity-50">
                <img src="path_to_inc_logo.png" alt="Inc." class="h-12 opacity-50">
            </div>
        </section>
    </main>

    <footer class="bg-gray-800 py-4 mt-16">
        <div class="container mx-auto text-center">
            <p>&copy; 2023 Heartland SEO. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
