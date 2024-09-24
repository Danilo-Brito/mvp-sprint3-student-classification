/*
  --------------------------------------------------------------------------------------
  Função com requisição GET que retorna todos os estudantes do banco de dados
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/students';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      data.students.forEach(item => insertList(
        item.name,
        item.gender,
        item.attendance_rate,
        item.study_hours_per_week,
        item.previous_grade,
        item.extracurricular_activities,
        item.parental_support,
        item.final_grade
      ))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um item na lista via POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (
  name, gender, attendanceRate, studyPerWeek, previousGrade, extraActivities, parentalSupport
) => {
  const formData = new FormData();
  formData.append('name', name);
  formData.append('gender', gender);
  formData.append('attendance_rate', attendanceRate);
  formData.append('study_hours_per_week', studyPerWeek);
  formData.append('previous_grade', previousGrade);
  formData.append('extracurricular_activities', extraActivities);
  formData.append('parental_support', parentalSupport);

  let url = 'http://127.0.0.1:5000/add_student';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => {
      response.json()
      alert("Aluno inserido na basa de dados")
      console.log(response.json())
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista via DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/delete_student?name=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados.
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista
  --------------------------------------------------------------------------------------
*/
const insertList = (name, gender, attendanceRate, studyPerWeek, previousGrade, extraActivities, parentalSupport, finalGrade) => {
  var item = [name, gender, attendanceRate, studyPerWeek, previousGrade, extraActivities, parentalSupport, finalGrade];
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  formatData(item)

  for (var i = 0; i < item.length; i++) {
    var cell = row.insertCell(i);
    cell.textContent = item[i];
  }

  var deleteCell = row.insertCell(-1);
  insertDeleteButton(deleteCell);


  document.getElementById("name").value = "";
  document.getElementById("gender").value = "";
  document.getElementById("attRate").value = "";
  document.getElementById("studyPWeek").value = "";
  document.getElementById("prevGrade").value = "";
  document.getElementById("extActivies").value = "";
  document.getElementById("parenSupport").value = "";

  removeElement();
}

/*
  --------------------------------------------------------------------------------------
  Função para formatar os dados de genero e apoio de parentes em string.
  --------------------------------------------------------------------------------------
*/
function formatData(item) {
  // Formantando gender: 0 = Male, 1 = Female
  if (item[1] === "0") {
    item[1] = "Male";
  } else if (item[1] === "1") {
    item[1] = "Female";
  }

  // Formantando parentalSupport: 0 = Low, 1 = Medium, 2 = High
  switch (item[6]) {
    case "0":
      item[6] = "Low";
      break;
    case "1":
      item[6] = "Medium";
      break;
    case "2":
      item[6] = "High";
      break;
  }

  return item;
}

/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item na lista
  --------------------------------------------------------------------------------------
*/
const newItem = async () => {
  let inputName = document.getElementById("name").value;
  let inputGender = document.getElementById("gender").value;
  let inputAttRate = document.getElementById("attRate").value;
  let inputStudyWeek = document.getElementById("studyPWeek").value;
  let inputPrevGrade = document.getElementById("prevGrade").value;
  let inputExtActivies = document.getElementById("extActivies").value;
  let inputParenSupport = document.getElementById("parenSupport").value;

  // Verificando se os campos estão vazios
  if (inputName === '') {
    alert("O nome do estudante não pode ser vazio!");
  } else if (inputGender === "" || inputAttRate === "" ||
    inputStudyWeek === "" || inputPrevGrade === "" ||
    inputExtActivies === "" || inputParenSupport === "") {
    alert("Todos os campos precisam estar preenchido");
  } else {

    // Formatando os dados string para int
    if (inputGender === "male") {
      inputGender = 0
    } else if (inputGender === "female") {
      inputGender = 1
    }

    switch (inputParenSupport) {
      case "low":
        inputParenSupport = "0";
        break;
      case "medium":
        inputParenSupport = "1";
        break;
      case "high":
        inputParenSupport = "2";
        break;
    }

    console.log(inputName, inputGender, inputAttRate, inputStudyWeek, inputPrevGrade, inputExtActivies, inputParenSupport)
    postItem(inputName, inputGender, inputAttRate, inputStudyWeek, inputPrevGrade, inputExtActivies, inputParenSupport);
  }
}