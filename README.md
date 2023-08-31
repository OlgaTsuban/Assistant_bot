# Assistant bot
<p>Here is the project "Assistant bot"</p>
<h2>Why we have 4 files? </h2>
<p>File main4.py has better functionality(I recommend you to use it), but others are working too.</p>
<p>Here is a description for each file.</p>
<h2>main1.py</h2>
<p>In the initial stage, our assistant bot is able to store a name and phone number, find a phone number by name, update a recorded phone number, and display all saved records in the console.</p>
<h2>main2.py</h2>
<p>Our assistant can already interact with the user using the command line, receiving commands and arguments and performing the required actions. In this program, we work on the internal logic of the assistant, focusing on how data is stored, what specific data is stored, and what can be done with it.

For these purposes, we apply object-oriented programming.

The user will have an address book or contact book. This contact book contains entries. Each entry contains a set of fields.</p>
<p>The user interacts with the contact book by adding, deleting, and editing entries. The user is also able to search for entries in the contact book using one or multiple criteria (fields).

Regarding fields, we can also say that they can be mandatory (such as name) and optional (such as phone or email). Entries can also contain multiple fields of the same type (multiple phone numbers, for example). The user has the ability to add/remove/edit fields in any entry.</p>
<h2>main3.py</h2>
<p>Here are the next upgrades:</p>
<ol>
  <li>Add functionality for working with the Birthday field in the Record class, specifically the "days_to_birthday" function, which returns the number of days until the next birthday.</li>
  <li>Add validation functionality to ensure the correctness of provided values for the Phone and Birthday fields.</li>
  <li>Implement pagination (page-by-page output) for the AddressBook in cases where the book is very large and needs to be displayed in parts rather than all at once. Achieve this by creating an iterator for the entries.</li>
</ol>
<h2>main4.py</h2>
<h1>What this project can do ?</h1>
<p>This is a console assistant bot that recognizes commands entered from the keyboard and responds accordingly to the entered command.
The assistant bot serves as a prototype for an assistant application. In its initial form, the assistant application is able to work with a contact book and a calendar.</p>
<p>The bot accepts the following commands:</p>
<ol>
  <li>"hello": Responds in the console with "How can I help you?"</li>
  <li>"add ...": With this command, the bot stores a new contact in memory (e.g., in a dictionary). Instead of ..., the user enters a name and phone number, separated by a space.</li>
  <li>"change ...": This command allows the bot to update the phone number of an existing contact. Instead of ..., the user enters a name and the new phone number, separated by a space.</li>
  <li>"phone ...": Using this command, the bot displays the phone number of the specified contact in the console. Instead of ..., the user enters the name of the contact whose number they want to show.</li>
  <li>"show all": With this command, the bot displays all saved contacts with their phone numbers in the console.</li>
  <li>"good bye", "close", "exit": The bot terminates its operation after displaying "Good bye!" in the console, upon receiving any of these commands.</li>
  
  <p>From main2.py </p>
  <li>"delete": With this command, the bot deletes contact's number in memory (e.g., in a dictionary). Instead of ..., the user enters a name and phone number, separated by a space.</li>
  
  <p>From main3.py</p>
  <li>"birth": With this command, the bot stores a new contact in memory (or modify if it already exists). Instead of ..., the user enters a name and birthday, separated by a space.</li>
  <li>"days": Using this command, the bot displays the amount of days till birthday of the specified contact in the console. Instead of ..., the user enters the name of the contact .</li>
  <li>"iteration": Using this command, the bot displays the amount of phone number of the phone book in the console. Instead of ..., the user enters the number, how many contacts the user wants to see .</li>
<h1>How to use?</h1>
<p>You can write this for MacOS <b>python3 main.py the/way/to/the/dir</b> </p>
<p>You can write this for Windows <b>python main.py C:the\way\to\the\dir</b> </p>
