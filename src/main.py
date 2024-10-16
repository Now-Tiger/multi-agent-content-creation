#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from crewai import Crew
from agents import ContentCreationAgents
from tasks import TaskScheduler

from IPython.display import Markdown


# 1. Instantiate agents
agent_instance = ContentCreationAgents()
planner_agent = ContentCreationAgents.plannerAgent(agent_instance)
writer_agent = ContentCreationAgents.writerAgent(agent_instance)
editor_agent = ContentCreationAgents.editorAgent(agent_instance)


# 2. Instatiate tasks
task_scheduler_instance = TaskScheduler()
planning_task = TaskScheduler.planningTask(task_scheduler_instance)
writing_task = TaskScheduler.writingTask(task_scheduler_instance)
editing_task = TaskScheduler.editingTask(task_scheduler_instance)


# 3. Create list of agents and tasks separately
agents_list = [planner_agent, writer_agent, editor_agent]
tasks_list = [planning_task, writing_task, editing_task]


# 4. Create crew object of agents and task to perform
crew = Crew(agents=agents_list, tasks=tasks_list, verbose=2)


# 5. Lauch crew
result = crew.kickoff(inputs={"topic": "Artifical Intelligence"})
Markdown(result)