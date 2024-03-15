from functools import partial
from crewai import Task
from textwrap import dedent


class YoutubeAutomationTasks():

    def manage_youtube_video_creation(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Oversee the YouTube prepration process including market research, title ideation, 
                description creation, and email creation reqired to make a YouTube video. The ultimate goal is for you to generate 
                a report including a research table, potential high click-through-rate titles, 
                a YouTube video description, and an emails newsletter update about the new video.
                               
                The video topic is: {video_topic}
                The video details are: {video_details}

            Example Output:
                                   
            # YouTube Competition Research Table:
            - Video 1:
                - Title: "How to Make a YouTube Video"
                - View Count: 100,000
                - Days Since Published: 30
                - Channel Subscriber Count: 1,000
                - Video URL: https://www.youtube.com/watch?v=1234
            - Video 2:
                - Title: "How to Make a YouTube Video"
                - View Count: 100,000
                - Days Since Published: 30
                - Channel Subscriber Count: 1,000
                - Video URL: https://www.youtube.com/watch?v=1234

            [THE REST OF THE YOUTUBE COMPETITION RESEARCH GOES HERE]
                                   
            - Video 15:
                - Title: "How to Make a YouTube Video"
                - View Count: 100,000
                - Days Since Published: 30
                - Channel Subscriber Count: 1,000
                - Video URL: https://www.youtube.com/watch?v=1234                
                                   
            # Potential High CTRO Titles:
            - How to Make a YouTube Video
            - How to Make a YouTube Video in 2021
            - How to Make a YouTube Video for Beginners
            [THE REST OF THE POTENTIAL HIGH CTRO TITLES GO HERE]
                                   
            # YouTube Video Description:
            🤖 Download the CrewAI Source Code Here:
            https://brandonhancock.io/crewai-updated-tutorial-hierarchical 

            Don't forget to Like and Subscribe if you're a fan of free source code 😉

            Ready to lead an AI revolution? Watch and learn how to build your own CrewAI from the ground up using the latest CrewAI features, and get set to deploy an army of AI agents at your command. This video is your ultimate guide to creating a powerful digital workforce, enhancing your projects with intelligent automation and streamlined workflows. Discover the secrets to customizing AI agents, setting them on tasks, and managing a smooth operation with CrewAI. It’s time to amplify your tech capabilities, and after this tutorial, you'll be equipped to engineer an AI crew that transforms any complex challenge into a simple task. Start your journey to AI mastery with CrewAI today!

            📰 Stay updated with my latest projects and insights:
            LinkedIn: https://www.linkedin.com/in/brandon-hancock-ai/
            Twitter: https://twitter.com/bhancock_ai

            Resources:
            - https://github.com/joaomdmoura/crewAI-examples/
            - https://www.crewai.io/
            - https://twitter.com/joaomdmoura/status/1756428892045496608
            - https://serper.dev/
            
            # Email Announcement:
            
            Subject: New UX UI Design Tutorial: Learn How To Use the Latest Figma Features

            Hey [FIRST NAME GOES HERE]!

            Exciting update: Figma's new version is here, making it quicker and more dependable!

            You loved our first Figma tutorial, so I just published a new one for you.

            In this tutorial, you'll get up to speed with CrewAI's new features. We'll then apply these updates by building an AI Newsletter, demonstrating how to use what you've learned in a real project.

            [VIDEO PREVIEW HERE]

            Here's what's in store:

            Learn to manage a team with Figma's new multi edit feature.
            Discover how asynchronous tasks can boost your efficiency.
            Find out how the Expected Output feature ensures accuracy and reliability.
            Plus, lots more insights!
            Dive into the tutorial to explore Figma's enhanced functions:

            [VIDEO PREVIEW HERE]

            Questions or want to share how you're doing? Email me or comment on YouTube.

            Happy coding!

            Cheers, 
            Brandon Hancock
            """),
            agent=agent,
            expected_output="A refined finalized version of the youtube video research, youtube video title, youtube video description, and new youtube video email anouncement in markdown format",
            output_file="output/YouTube_Video_Creation_Report"
        )

    def manage_youtube_video_research(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""For a given video topic and description, search youtube videos to find 
                5 high-performing YouTube videos on the same topic. Once you have found the videos, 
                research the YouTube video details to finish populate the missing fields in the 
                research CSV. When delegating tasks to other agents, make sure you include the 
                URL of the video that you need them to research.
                            
                This research CSV which will be used by other agents to help them generate titles 
                and other aspects of the new YouTube video that we are planning to create.
                               
                Research CSV Outline:
                - Title of the video
                - View count
                - Days since published
                - Channel subscriber count
                - Video URL
                       
                The video topic is: {video_topic}
                The video details is: {video_details}

                Important Notes: 
                - Make sure the CSV uses ; as the delimiter
                - Make sure the final Research CSV Outline doesn't contain duplicate videos
                - It is SUPER IMPORTANT that you only populate the research CSV with real YouTube videos 
                    and YouTube URLs that actually link to the YouTube Video.
                """),
            agent=agent,
            expected_output=dedent(f"""
                Video Title; View Count; Days Since Published; Channel Subscriber Count; Video URL
                How to Make a YouTube Video; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                How to Get Your First 1000 Subscribers; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                       ...              
                """)
        )

    def create_youtube_video_title(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Create 5 potential titles for a given YouTube video topic and description. 
                It is also very important to use researched videos to help you generate the titles.
                The titles should be less than 70 characters and should have a high click-through-rate.
                               
                Video Topic: {video_topic}
                Video Details: {video_details}
                """),
            agent=agent,
            expected_output=dedent(f"""
                - UX UI Tutorial for Beginners: Learn How To Use Latest CrewAI Features
                - UX UI Tutorial: Complete Crash Course for Beginners
                - How to design landing page using Figma
                - How to Use Figma to prototype mobile app
                - Figma Tutorial: How to Build a Shopify website design
                ...                
                """),
        )

    def create_youtube_video_description(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Create a description for a given YouTube video topic and description.     
                Video Topic: {video_topic}
                Video Details: {video_details}
                """),
            agent=agent,
            expected_output=dedent(f"""
                🤖 Download the Figma Source File Here:
                https://leveling.app/templates/cosmo-shopify-template
                                   
                Don't forget to Like and Subscribe if you're a fan of free source file 😉
                                   
                Want to join a community of AI developers? Join the UX UI Design Skook Community for FREE:
                https://www.skool.com/ux-ui-design

                Ready to lead the UX UI Design Career? Watch and learn how to build your real life project from the ground up using the latest Figma features, and get set to deploy an army of AI agents at your command. This video is your ultimate guide to creating a powerful digital workforce, enhancing your projects with intelligent automation and streamlined workflows. It’s time to amplify your tech capabilities, and after this tutorial, you'll be equipped to designer / beginner an project that ready to put to your portfolio. Start your journey to UX UI design with Figma today!

                📰 Stay updated with my latest projects and insights:
                LinkedIn: https://www.linkedin.com/company/leveling/
                Twitter: https://twitter.com/leveling_app

                Resources:
                [LEAVE BLANK]
                                   
                Timestamps: 
                [LEAVE BLANK]
            """),
        )

    def create_email_announcement_for_new_video(self, agent, video_topic, video_details):
        return Task(
            description=dedent(f"""Create an email to send to an email list to promote the new YouTube video.
                               
                Video Topic: {video_topic}
                Video Details: {video_details}

                Here are a few previous email announcements that you can use as inspiration. 
                
                Important Notes:
                - Make sure to copy my style, tone, and voice when writing the email.
                -  Before submitting your final work, you MUST have a human review your tenative final email.

                Email 1:
                ----------------
                Subject: New UX UI Tutorial: Learn How To Use the Latest Figma Features

                Hey [FIRST NAME GOES HERE]!

                Exciting update: Figma's new version is here, making it quicker and more dependable!

                You loved our first Figma tutorial, so I just published a new one for you.

                In this tutorial, you'll get up to speed with Figma's new features. We'll then apply these updates by building an Creative Agency Website Design, demonstrating how to use what you've learned in a real project.

                video preview​
                Here's what's in store:

                Learn to manage a team with Figma's new multi edit feature.
                Discover how multi editing can boost your efficiency.
                Find out how the Expected Output feature ensures accuracy and reliability.
                Plus, lots more insights!
                Dive into the tutorial to explore Figma's enhanced functions:

                video preview​
                Questions or want to share how you're doing? Email me or comment on YouTube.

                Happy coding!

                Cheers, 
                Leo from Leveling
                ----------------
                """),
            agent=agent,
            expected_output="A refined finalized version of a new youtube video email anouncement in markdown format",
        )
