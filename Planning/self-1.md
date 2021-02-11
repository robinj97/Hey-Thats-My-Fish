## Self-Evaluation Form for Milestone 1

### General 

We will run self-evaluations for each milestone this semester.  The
graders will evaluate them for accuracy and completeness.

Every self-evaluation will go out into your Enterprise GitHub repo
within a short time afrer the milestone deadline, and you will have 24
hours to answer the questions and push back a completed form.

This one is a practice run to make sure you get


### Specifics 


- does your analysis cover the following ideas:

  - the need for an explicit Interface specification between the (remote) AI 
    players and the game system?
        
        No, in our design logic, we were aware that there would need to be some sort of referee system, but we
        made the wrong assumption that server side would be handled already and that we were to make a game that just 
        connected to the server and followed certain rules, but that the server had some sort of system to double check.
        However we did not explicitly specify that there needs to be some interface linking them together.



  - the need for a referee sub-system for managing individual games
  
        Yes we were aware that we needed a referee sub system to manage the game rules. In our thought process when 
        discussing the MVC model, we did not specifically call it a referee but we referred to it as the logic and ruleset.
        We outlined that this would be something to implement in the model that acts as a validator / referee.



  - the need for a tournament management sub-system for grouping
    players into games and dispatching to referee components
    
        No we did not consider this. This is actually a great point that we will keep in mind going forward. Our thought
        process was more along the lines of keeping track of player data and having some way of distributing the players
        but we did not think about the dispatching of referee components. This is something that when we read in the self-eval
        points that we definitely did not think of and have learned that it is something we should be thinking of.
        



- does your building plan identify concrete milestones with demo prototypes:

  - for running individual games
  
        Yes our plan has concrete steps on how to demo localized first, and then server based. Our milestones state that 
        with each component that gets finished, there would be a demo that is interactable and not just a static image.




  - for running complete tournaments on a single computer 
  
        No. We assumed that this is something Khoury servers would have set up for us for example. We did not assume that
        we were in charge of setting up the tournaments, only that we were able to connect to the tournaments and sign up.
        I feel like maybe we misunderstood here and should have accounted for this, and set up a plan to create the server
        logic as well.




  - for running remote tournaments on a network
 
    
    Yes, we did take into account this as in our last milestone we state that the network side of things would be finalized.
    This would include remote tournaments.




- for the English of your memo, you may wish to check the following:

  - is each paragraph dedicated to a single topic? does it come with a
    thesis statement that specifies the topic?
    
        Most paragraphs follow paragraph structure. Each paragraph pertains to one idea or train of thought.




  - do sentences make a point? do they run on?
  
        Sentences do make a clear and concise point. There is no confusion and we structured it in a memo way that isn't
        too technical in case a non technical person were to read as well.




  - do sentences connect via old words/new words so that readers keep
    reading?
    
        Yes. There is a natural flow of sentences that do not feel too segmented. As mentioned earlier, clear and concise.
        We wrote it such that its structure follows logically as our thoughts develop. 
    
        




  - are all sentences complete? Are they missing verbs? Objects? Other
    essential words?
    
        No.



  - did you make sure that the spelling is correct? ("It's" is *not* a
    possesive; it's short for "it is". "There" is different from
    "their", a word that is too popular for your generation.)
    
        Yes we made sure that there were no spelling errors. We wrote it in Word and used the spell checker, as well
        as proof-reading.



The ideal feedback are pointers to specific senetences in your memo.
For PDF, the paragraph/sentence number suffices. 

For **code repos**, we will expect GitHub line-specific links. 


