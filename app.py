from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# HTML templates as strings
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Use Comic Sans Neo font */
        @import url('https://fonts.googleapis.com/css2?family=Comic+Sans+MS:wght@400;700&display=swap');

        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            background: linear-gradient(to right, #e0eafc, #cfdef3);
        }
        .container {
            margin-top: 150px;
            padding-top: 10px;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            position: relative;
            flex: 1;
            padding: 10px;
            box-sizing: border-box;
        }
        .login-container, .resources-page {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
            padding: 20px;
            width: 90%;
            max-width: 800px;
            text-align: center;
            z-index: 1;
            animation: fadeIn 1s ease-in-out;
        }
        .login-container h1, .resources-page .title {
            color: #333;
            font-size: 2em;
        }
        input[type="password"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background: linear-gradient(135deg, #6a1b9a, #ab47bc);
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            font-size: 1em;
        }
        button:hover {
            background: linear-gradient(135deg, #4a148c, #9c27b0);
            transform: scale(1.05);
        }
        .resources-page {
            display: none;
            width: 100%;
            max-width: 800px;
            padding: 20px;
            text-align: center;
        }
        .nav-bar {
            position: sticky;
            top: 15px;
            left: 0;
            width: 100%;
            background-color: #fafafa;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            z-index: 2;
            display: flex;
            justify-content: space-around;
            padding: 10px;
            border-radius: 8px;
            box-sizing: border-box;
            margin-bottom: 20px;
        }
        .nav-bar a {
            text-decoration: none;
            color: #6a1b9a;
            font-weight: bold;
            padding: 10px;
            font-size: 1.1em;
        }
        .nav-bar a:hover {
            text-decoration: underline;
        }
        .resource-content {
            display:none;
        }
        .resource {
            display: block;
            margin: 20px 0;
            text-align: center;
            animation: slideUp 0.5s ease-out forwards;
        }
        .resource img {
            width: 150px;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }
        .resource img:hover {
            transform: scale(1.1);
        }
        .resource-title {
            font-size: 1.5em;
            margin: 10px 0;
            color: #333;
        }
        .resource-description {
            font-size: 1em;
            margin: 10px 0;
            color: #666;
        }
        .contact-support {
            margin-top: 30px;
            font-size: 1em;
            color: #999;
        }
        .contact-support a {
            color: #ab47bc;
            text-decoration: none;
        }
        .contact-support a:hover {
            text-decoration: underline;
        }
        .error-message {
            color: red;
            margin-top: 10px;
            display: none;
        }
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.7);
            z-index: 0;
            display: none;
            align-items: center;
            justify-content: center;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideUp {
            from { transform: translateY(100%); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes slideDown {
            from { transform: translateY(0); opacity: 1; }
            to { transform: translateY(-100%); opacity: 0; }
        }
        #instagram-section {
            margin-top: 400px;
        }
#telegram-section {
            margin-top: 50px;
        }
#whatsapp-section {
            margin-top: 400px;
        }
    </style>
</head>
<body>
    <div class="overlay" id="overlay"></div>
    <div class="container">
        <div class="login-container" id="login-container">
            <form onsubmit="return validatePassword(event)" method="post">
                <h1>Login</h1>
                <input type="password" id="password" name="password" placeholder="Enter Password" required><br><br>
                <button type="submit">NEXT</button>
                <div id="error-message" class="error-message"><br>Incorrect password</div>
            </form>
        </div>
        <div class="resources-page" id="resources-page">
            <div class="nav-bar">
                <a href="#" onclick="showPage('instagram-section'); return false;">Instagram</a>
                <a href="#" onclick="showPage('telegram-section'); return false;">Telegram</a>
                <a href="#" onclick="showPage('whatsapp-section'); return false;">WhatsApp</a>
            </div>
            <div id="instagram-section" class="resource-content">
                <div class="title">Instagram Resources<br> (From 12/4/2024 to 22/7/2024)</div>
                <div class="resource">
                    <div class="resource-title">PHOTOS</div>
                    <div class="resource-description">Click the thumbnail to view Photos PDF👇🏼</div>
                    <a href="https://drive.google.com/file/d/1ET5Noy5SiQJXXPzXxSgQ3d9MM-szl9Av/view?usp=drivesdk" target="_blank">
                        <img src="IP1.png" alt="Instagram Photo 1 Thumbnail">
                    </a>
                </div>
                <div class="resource">
                    <div class="resource-title">VIDEOS</div>
                    <div class="resource-description">Click the thumbnail to get redirected to the Videos Page👇🏼</div>
                    <a href="videos.html" target="_blank">
                        <img src="instagram_video1_thumbnail.jpg" alt="Instagram Video 1 Thumbnail">
                    </a>
                </div>
                <div class="resource">
                    <div class="resource-title">TEXT MESSAGES</div>
                    <div class="resource-description">Click the thumbnail to view text Messages PDF👇🏼</div>
                    <a href="instagram_texts.pdf" target="_blank">
                        <img src="IT1.jpg" alt="Instagram Texts Thumbnail">
                    </a>
                </div>
            </div>
            <div id="telegram-section" class="resource-content">
                <div class="title">Telegram Resources</div>
                <div class="resource">
                    <div class="resource-title">Telegram (1)<br>22/10/23 to 1/5/24</div>
                    <div class="resource-description">Click the thumbnail to access the PDF👇🏼</div>
                    <a href="https://drive.google.com/file/d/1GmTR72aU4IieS4uhXAR2MP2vv4Jx6K65/view?usp=drivesdk" target="_blank">
                        <img src="T1.png" alt="Telegram Document Thumbnail">
                    </a>
                </div>
            </div>
           <div id="whatsapp-section" class="resource-content">
                <div class="title">WhatsApp Resources</div>
                <div class="resource">
                    <div class="resource-title">Deepali_Bitanu (1) <br> 20/11/22 to 12/11/23</div>
                    <div class="resource-description">Click the thumbnail to access the PDF👇🏼</div>
                    <a href="https://drive.google.com/file/d/13ZIpohKWMSx1glknKoOfoSbDfuKdmo8J/view?usp=drivesdk" target="_blank">
                        <img src="D1.png" alt="Deepali_Bitanu (1) Thumbnail">
                    </a>
                </div>
                <div class="resource">
                    <div class="resource-title">Deepali_Bitanu (2)<br>22/3/24 to 4/4/24(3:34 PM)</div>
                    <div class="resource-description">Click the thumbnail to access the PDF👇🏼</div>
                    <a href="https://drive.google.com/file/d/1G0TcqizBRVHuL09iQDKkuHVnh-qV4MJl/view?usp=drivesdk" target="_blank">
                        <img src="D2.png" alt="Deepali_Bitanu (2) Thumbnail">
                    </a>
                </div>
                <div class="resource">
                    <div class="resource-title">Deepali_Bitanu (3)<br>4/4/24 to 11/6/24</div>
                    <div class="resource-description">Click the thumbnail to access the PDF👇🏼</div>
                    <a href="https://drive.google.com/file/d/1EX4H36FmRoE8zMvPylPe-AnZhN3wdDRw/view?usp=drivesdk" target="_blank">
                        <img src="D3.png" alt="Deepali_Bitanu (3) Thumbnail">
                    </a>
                </div>
            </div>
            <div class="contact-support">
                For any issues, contact support at <a href="mailto:support@example.com">support@example.com</a>.
            </div>
        </div>
    </div>

    <script>
        var overlay = document.getElementById("overlay");

        function validatePassword(event) {
            event.preventDefault();

            var passwordInput = document.getElementById("password").value;
            var correctPassword = "217";

            if (passwordInput === correctPassword) {
                document.getElementById("login-container").style.display = "none";
                document.getElementById("resources-page").style.display = "block";
                return false;
            } else {
                document.getElementById("error-message").style.display = "block";
                return false;
            }
        }

        function showPage(pageId) {
    var contents = document.getElementsByClassName("resource-content");
    for (var i = 0; i < contents.length; i++) {
        if (contents[i].style.display !== "none") {
            contents[i].style.animation = 'slideDown 0.5s ease-out';
            setTimeout(function(content) {
                content.style.display = "none";
                content.style.animation = '';
            }, 500, contents[i]);
        }
    }

    setTimeout(function() {
        var pageToShow = document.getElementById(pageId);
        pageToShow.style.display = "block";
        pageToShow.style.animation = 'slideUp 0.5s ease-out';
        setTimeout(function() {
            pageToShow.style.animation = '';
            // Scroll to the top of the newly displayed section with an offset
            window.scrollTo({
                top: pageToShow.offsetTop - 50, // Adjust the offset value as needed
                behavior: 'smooth'
            });
        }, 500);
    }, 500);
}



        window.addEventListener('beforeunload', function (e) {
            e.preventDefault();
            e.returnValue = '';
            lockWindow();
        });

        document.addEventListener('visibilitychange', function() {
            if (document.visibilityState === 'hidden') {
                lockWindow();
            } else if (document.visibilityState === 'visible') {
                unlockWindow();
            }
        });

        window.addEventListener('blur', function() {
            lockWindow();
        });

        window.addEventListener('focus', function() {
            unlockWindow();
        });

        window.addEventListener('contextmenu', function (e) {
            e.preventDefault();
            lockWindow();
        });

        function lockWindow() {
            document.getElementById("login-container").style.display = "none";
            document.getElementById("resources-page").style.display = "none";
            document.getElementById("password").value = "";
            document.activeElement.blur();
            overlay.style.display = "block";
        }

        function unlockWindow() {
            document.getElementById("login-container").style.display = "block";
            document.getElementById("resources-page").style.display = "none";
            overlay.style.display = "none";
        }
    </script>
</body>
</html>"""









VIDEOS_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .video-container {
            width: 90%;
            max-width: 1200px;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
        }
        .video {
            width: calc(33.333% - 30px);
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            position: relative;
            cursor: pointer;
        }
        .video video {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .video-title {
            padding: 10px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }
        .video-description {
            padding: 0 10px 10px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }
        .popup-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        .popup-content {
            position: relative;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .popup-content video {
            max-width: 90vw;
            max-height: 90vh;
        }
        .popup-close {
            position: absolute;
            top: -22px;
            right: 4px;
            font-size: 18px;
            color: white;
            cursor: pointer;
            background: #ff0000;
            padding: 7px 15px;
            border: none;
            border-radius: 5px;
        }
        @media (max-width: 768px) {
            .video {
                width: calc(50% - 30px);
            }
        }
        @media (max-width: 480px) {
            .video {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="video-container">
        <!-- Repeat this block for each video -->
        <div class="video" onclick="showPopup('vid1.mp4')">
            <video>
                <source src="vid1.mp4#t=10" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <div class="video-title">Video Title 1</div>
            <div class="video-description">Video Description 1</div>
        </div>
        <div class="video" onclick="showPopup('videos/video2.mp4')">
            <video>
                <source src="videos/video2.mp4#t=10" type="video/mp4">
                Your browser does not support the video tag.
            </video>
            <div class="video-title">Video Title 2</div>
            <div class="video-description">Video Description 2</div>
        </div>
        <!-- Add more video blocks as needed -->
    </div>

    <div class="popup-overlay" id="popup-overlay">
        <div class="popup-content">
            <button class="popup-close" onclick="closePopup()">Close</button>
            <video id="popup-video" controls>
                <source id="popup-video-source" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
    </div>

    <script>
        function showPopup(videoSrc) {
            var overlay = document.getElementById('popup-overlay');
            var video = document.getElementById('popup-video');
            var videoSource = document.getElementById('popup-video-source');

            videoSource.src = videoSrc;
            video.load();
            overlay.style.display = 'flex';
        }

        function closePopup() {
            var overlay = document.getElementById('popup-overlay');
            overlay.style.display = 'none';
            var video = document.getElementById('popup-video');
            video.pause(); // Pause video when closing popup
        }

        // Close popup if the overlay itself is clicked
        document.getElementById('popup-overlay').addEventListener('click', function(e) {
            if (e.target === this) {
                closePopup();
            }
        });
    </script>
</body>
</html>"""


@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = ''
    if request.method == 'POST':
        password = request.form.get('password')
        if password != 'expected_password':  # Replace 'expected_password' with your actual password
            error_message = 'Incorrect password'
        else:
            return redirect(url_for('resources_page'))
    return render_template_string(HTML_TEMPLATE, error_message=error_message)

@app.route('/resources')
def resources_page():
    return render_template_string(HTML_TEMPLATE, error_message="")

@app.route('/videos')
def videos():
    return render_template_string(VIDEOS_HTML)

