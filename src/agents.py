#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

from crewai import Agent
from langchain_groq import ChatGroq


# Load .env: environment variables.
load_dotenv()


class ContentCreationAgents(object):
  """
  Multi-agent workflow for content creation.
  Here creating 3 agents, each having specific responsibility in the content creation task.
  """
  def __init__(self) -> None:
    self.llm = ChatGroq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API"), temperature=0.1)
    self.planner = "Content Planner"
    self.writer  = "Content Writer"
    self.editor  = "Editor"

  def plannerAgent(self) -> None:
    return Agent(
      llm=self.llm,
      role=self.planner,
      goal="Plan engaging and factually accurate content on {topic}",
      backstory="""
      you're working on planning a blog article about the topic: {topic}. 
      You collect information that helps the audience learn something and make informed decisions. 
      Your work is the basis for the Content Writer to write an article on this topic.
      """,
      allow_deligation=False,
      verbose=True,
      max_iter=1,
    )
  
  def writerAgent(self) -> None:
    return Agent(
      llm=self.llm,
      role=self.writer,
      goal="Write insightful and factually accurate opinion piece about the topic: {topic}",
      backstory="""
      You're working on a writing a new opinion piece about the topic: {topic}.
      You base your writing on the work of the Content Planner, who provides an outline and relevant context about the topic.
      You follow the main objectives and direction of the outline, as provide by the Content Planner.
      You also provide objective and impartial insights and back them up with information provide by the Content Planner.
      You acknowledge in your opinion piece when your statements are opinions as opposed to objective statements.
      """,
      allow_deligation=False,
      verbose=True,
      max_iter=1,
    )
  
  def editorAgent(self) -> None:
    return Agent(
      llm=self.llm,
      role=self.editor,
      goal="Edit the given blog post to align with the writing style of the organization",
      backstory="""
      You are an editor who receives a blog post from the Content Writer.
      Your goal is to review the blog post to ensure that it follows journalistic best practices, provides balanced viewpoints 
      when providing opinions or assertions, and also avoids major controversial topics or opinions when possible.
      """,
      allow_deligation=False,
      verbose=True,
      max_iter=1,
    )
