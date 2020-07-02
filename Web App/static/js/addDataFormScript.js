var closebtns = document.getElementsByClassName("close");
var i;
var skillArray = [];
var addSkillBtn = document.getElementById("add-skill-btn");
var addSkill = document.getElementById("add-skill");
var skillList = document.getElementById("skill-list");

addSkillBtn.addEventListener('click', (e)=>{
    e.preventDefault();
    const skill = addSkill.value;
    if(skill != '' && !skillArray.includes(skill)){
    skillArray.push(skill);
    skillList.innerHTML+=`<li>${skill}<span class="close">&times;</span></li>`;
    }
});


skillList.addEventListener('click', (e)=>{
    if(e.target.classList.contains("close")){
        e.target.parentElement.style.display = 'none';
        const skill = e.target.parentElement.textContent;
        skillArray.splice( skillArray.indexOf(skill), 1 );
        console.log(skillArray);
        // for( var i = 0; i < skillArray.length; i++){ 
        //     if ( skillArray[i] === skill) { 
        //         skillArray.splice(i, 1); 
        //     }
        // }
    }
    
});


for (i = 0; i < closebtns.length; i++) {
  closebtns[i].addEventListener("click", function(e) {
    this.parentElement.style.display = 'none';
    console.log(e.target.parentElement.textContent);
  });
}

var skillString = document.getElementById("skillString");

function setSkillString(){

  console.log(skillArray);    

  tempSkillString = skillArray[0];
  tempSkillString = tempSkillString.concat("$");

  for (var i = 1; i<skillArray.length; i++){
    tempSkillString = tempSkillString.concat(skillArray[i]);
    tempSkillString = tempSkillString.concat("$");
  }

  skillString.setAttribute("value", tempSkillString)
  console.log(tempSkillString);
    
}