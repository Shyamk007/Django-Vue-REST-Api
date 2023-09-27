<template>
      <div id="app">
        <form @submit.prevent="submitForm">
      <div class="form-group">
        <input type="text" class="form-control" placeholder="Name" v-model="student.name">
        <input type="text" class="form-control" placeholder="Course" v-model="student.course">
        <input type="text" class="form-control" placeholder="Rating" v-model="student.rating">
        <button type="submit" class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Course</th>
          <th>Ranking</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student=student">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td><button class="btn btn-outline-danger btn-sm mx-1" @click="deleteStudent(student)">Delete</button></td>
        </tr>
      </tbody>
    </table>
      </div>
</template>

<script>
export default {
  name : 'App',
  data(){
    return{
      student:{
        name:'',
        course:'',
        rating:'',
      },
      students : []
    }
  },
  async created(){
    await this.getStudents();
  },
  methods: {
    submitForm(){
      if(this.student.id===undefined){
        this.createStudent();
      }else{
        this.editStudent();
      }
    },
    async getStudents(){
      var response = await fetch('http://localhost:8000/api/students/')
      this.students = await response.json()
    },

    async createStudent() {

      await this.getStudents();
      
      await fetch('http://localhost:8000/api/students/', {
        method: 'POST',
        body: JSON.stringify(this.student),
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      await this.getStudents(); 
    },
    async editStudent(){

      await this.getStudents();
      
      await fetch(`http://localhost:8000/api/students/${this.student.id}/`, {
        method: 'PUT',
        body: JSON.stringify(this.student),
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      await this.getStudents();
      this.student = {};

    },
    async deleteStudent(student){
      await this.getStudents();
      
      await fetch(`http://localhost:8000/api/students/${student.id}/`, {
        method: 'DELETE',
        body: JSON.stringify(this.student),
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      await this.getStudents();

    }
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.form-group {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

.form-group input {
  flex-basis: 33%;
  margin-right: 10px;
}


.table {
  margin-top: 20px;
  width: 100%;
  border-collapse: collapse;
}

.table thead th {
  background-color: #f2f2f2;
  padding: 10px;
  text-align: center;
}

.table tbody tr {
  border-bottom: 1px solid #ddd;
}

.table tbody td {
  padding: 10px;
  text-align: center;
}
</style>