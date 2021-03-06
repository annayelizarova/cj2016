# cj2016

# Concept and documentation


## App name: Out of sight, out of mind
(http://drones.pitchinteractive.com/)


## Elevator pitch

Since 2004, the USA has been practicing a new kind of military operation - using drones to take out enemy targets. The cost on civilian lives is pretty high and the data isn't made publically available by the government.
The data is manually collected by ground reporters. A good visualization of the air strikes and the deaths can really help put this in perspective and create empathy for those "out of sight"

## Inspirations and Prior Work

- [US gun killings](guns.periscopic.com)
+ This visualisation also focuses on deaths
+ It heavily relies on the animation to tell a story
+ The data is also congregate by a lot of individual news stories
+ The aestetic is very similar

# Data

## Data sources

1. [US gun killings](guns.periscopic.com)
2. [Bing News API](https://code.msdn.microsoft.com/bing)
3. [New America Foundation](http://counterterrorism.newamerica.net/about/militants)
4. [Living under drones](http://www.livingunderdrones.org/)

## Consistency among datasets

The challenge is that stories and estimates vary between sources. In cases where there are inconsistencies, a minimum and a maximum number of possible fatalities are recorded. We take the average whole number between these estimates for each attack. In a few instances there were fatalities confirmed, but the estimated number of fatalities was not obtainable. In these cases, we simply omitted the fatalities. The list of high-profile targets (the white squares) comes from the New America Foundation.


# Filtering options

## Attributes to search/find by

- Allow the user to jump from the attack view and the victim view
- Refreshing the page and watching the animation gives a good visualisation of time
- Hovering over gives more specifics on each day's count


# Views and Routes



# Visualizations
We have two main views - an attack view and a victim view. The two views aren't too different in content, but create a powerfull effect. 
The attack view shows you a birds eye view of all the data from 2004 to 2015, with something of the likes of a bar chart, while the victim view really zooms in on each individual day and breaks down each bar into concrete individuals as points.
A big part of the visalisation is watch the animation unfold over time


## Charts

The chart is layed out chronologically with each day displying the number of deaths - its a timeline. At the top there is also a visualisation of the breakdown of deaths that's animated to give you stats as you watch the chronological events unfold



## Tables

I wasn't sure how to attatch an image, but there is a table of all the news sources/articles used in the calculation of deaths





# Deployment

The visualization is created in HTML5 and JavaScript
Blah blah I put it up on Amazon EC2 or something...
