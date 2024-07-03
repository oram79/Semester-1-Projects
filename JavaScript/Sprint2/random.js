fetch('./players.json')
  .then(response => response.json())
  .then(data => {
    
    const container = document.createElement('div');
    container.id = 'playersContainer'

    data.forEach(players => {

      const playersDiv = document.createElement('div');
      playersDiv.className = 'players';

      playersDiv.innerHTML = `
        <h1>${getfullname(players)}</h1>
        <p>Player Age: ${getAge(players)}</p>
        <p>Player #: ${players.jerseynumber}</p>
        <p>Position: ${players.position}</p>
        <p>Goals: ${players.goals}</p>
        <p>Assisits: ${players.assists}</p>
        <p>Total Points: ${gettotalpoints(players)}</p>
        `;

        container.appendChild(playersDiv);
        
        // Logging Data To The Console
        console.log(getfullname(players));
        console.log(getAge(players));
        console.log(players.jerseynumber);
        console.log(players.position);
        console.log(players.goals);
        console.log(players.assists);
        console.log(gettotalpoints(players));
      });
    

      document.body.appendChild(container);
  })

  .catch(error => {
    // helping errors that occur while fetching the file
    console.error(error);
 });

// Fucntion List

function getfullname(players){
  return `${players.firstname} ${players.lastname}`;
}


function getAge(players){
  return `${players.firstname}'s ${new Date().getFullYear() - 
    new Date(players.birthday).getFullYear()} years old`;
}

function gettotalpoints(players){
  return Math.round(players.goals + players.assists);
}






