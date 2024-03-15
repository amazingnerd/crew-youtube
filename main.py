from crewai import Crew, Process

from agents import YoutubeAutomationAgents
from tasks import YoutubeAutomationTasks
from langchain_openai import ChatOpenAI
from tools.youtube_video_details_tool import YoutubeVideoDetailsTool
from tools.youtube_video_search_tool import YoutubeVideoSearchTool

from dotenv import load_dotenv
load_dotenv()


OpenAIGPT35 = ChatOpenAI(
    model="gpt-3.5-turbo"
)

agents = YoutubeAutomationAgents()
tasks = YoutubeAutomationTasks()

youtube_video_search_tool = YoutubeVideoSearchTool()
youtube_video_details_tool = YoutubeVideoDetailsTool()

youtube_manager = agents.youtube_manager()
research_manager = agents.research_manager(
    youtube_video_search_tool, youtube_video_details_tool)
title_creator = agents.title_creator()
description_creator = agents.description_creator()
email_creator = agents.email_creator()

# TODO: UPDATE THE VIDEO DETAILS - The purpose of this video is to talk about how I've automated my YouTube video creation process using CrewAI, cover new CrewAI features, and how to build custom CrewAI tools

video_topic = "UX UI Design tutorial for beginner"
video_details = """
In this video, we're learning superfast way to create an agency website design using Figma. From designing some of the most popular components and sections in landing page design to create power functional prototype, the newest version of Figma 2024 is revolutionizing how I create website design. But that's not all - I'm also showing you how to create an draft UX design from the beginning to production ready stunning UI design in just this 1 super fast course. Join me on this course as I unlock the potential of new Figma's features to enhance our design process and handoff more efficient with our development team like never before.
"""

manage_youtube_video_creation = tasks.manage_youtube_video_creation(
    agent=youtube_manager,
    video_topic=video_topic,
    video_details=video_details
)
manage_youtube_video_research = tasks.manage_youtube_video_research(
    agent=research_manager,
    video_topic=video_topic,
    video_details=video_details,
)
create_youtube_video_title = tasks.create_youtube_video_title(
    agent=title_creator,
    video_topic=video_topic,
    video_details=video_details
)
create_youtube_video_description = tasks.create_youtube_video_description(
    agent=description_creator,
    video_topic=video_topic,
    video_details=video_details
)
create_email_announcement_for_new_video = tasks.create_email_announcement_for_new_video(
    agent=email_creator,
    video_topic=video_topic,
    video_details=video_details
)


# Create a new Crew instance
crew = Crew(
    agents=[youtube_manager,
            research_manager,
            email_creator,
            ],
    tasks=[manage_youtube_video_creation,
           manage_youtube_video_research,
           create_email_announcement_for_new_video],
    process=Process.hierarchical,
    manager_llm=OpenAIGPT35
)

# Kick of the crew
results = crew.kickoff()

print("Crew work results:")
print(results)
