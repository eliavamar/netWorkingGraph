# Networking Graph & Security
The project deals with network security, by learning the behavior of the network and identifying anomalies.
The code enables a better understanding of given data representing network traffic, by turning it into a graph using the Neo4j database at fast runtime, and by using machine learning algorithms without the need for code
![image](https://user-images.githubusercontent.com/74323809/185081625-ed632fe0-8158-48aa-8dae-c6f88e9eebb2.png)

**first step**
In the first step, the user must select the csv file showing network traffic that he would like to work with
The preliminary step to this step is the part in which the user must obtain data representing network traffic, analyze and understand it, convert it to a csv file (a simple command in Python) and load it into the api system.

**second step**
At this stage, the user must choose what he wants to do with the api interface, whether he wants to present the data in his possession by a graph, something that will allow him to understand it better and know everything that is required about it before performing the work, or he already wants to run the algorithms on it

**steps three and four**
*3.Machine learning algorithms*
If the user chooses to use machine learning algorithms, he must know the algorithms he wants, enter the appropriate parameters, and give the address to save the desired results. After confirmation, the interface will run the requested algorithm with the given parameters and save the results at the given address.
This part spares the user the hassle but does not spare him the basic understanding of machine learning

![image](https://user-images.githubusercontent.com/74323809/185081248-22788683-94e7-44c8-b5fa-6c14e0d488ea.png)


*4.graph with Neo4j*
If the user chooses to create a graph with the data he has, which represents network traffic, he can use the interface, choose the number of vertices he wants and the requested query. The interface will run immediately and open an html file that displays the data in graph form.
This process saves the very long running times of neo4j because the code is executed in Python, and saves the need for the user to learn and understand the neo4j language

![image](https://user-images.githubusercontent.com/74323809/185081343-399c52c8-3e4e-470b-8d8a-780e1d60f8fd.png)


