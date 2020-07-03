<template>
    <div>
      <h1></h1>
      <mu-container>
        <mu-flex justify-content="around" align-items="center">
        </mu-flex>
        <mu-flex align-items="center" style="padding-bottom: 34px;">
          <span style="margin-right: 16px;">Форма обучения:</span>
          <mu-radio v-model="contract" style="margin-right: 16px;" value=0 label="Все"></mu-radio>
          <mu-radio v-model="contract" style="margin-right: 16px;" value=1 label="Бюджет"></mu-radio>
          <mu-radio v-model="contract" style="margin-right: 16px;" value=2 label="Контракт"></mu-radio>
        </mu-flex>
        <mu-flex align-items="center" style="padding-bottom: 34px;">
          <span style="margin-right: 16px;">Тип поступления:</span>
          <mu-radio v-model="type" style="margin-right: 16px;" value=0 label="Все"></mu-radio>
          <mu-radio v-model="type" style="margin-right: 16px;" value=1 label="После 9-го класса"></mu-radio>
          <mu-radio v-model="type" style="margin-right: 16px;" value=2 label="После 11-го класса"></mu-radio>
        </mu-flex>
        <mu-flex align-items="center" style="padding-bottom: 34px;">
          <span style="margin-right: 16px;">Тип обучения:</span>
          <mu-radio v-model="form" style="margin-right: 16px;" value=0 label="Все"></mu-radio>
          <mu-radio v-model="form" style="margin-right: 16px;" value=1 label="Очная"></mu-radio>
          <mu-radio v-model="form" style="margin-right: 16px;" value=2 label="Очно-заочная"></mu-radio>
          <mu-radio v-model="form" style="margin-right: 16px;" value=3 label="Заочная"></mu-radio>
        </mu-flex>
        <mu-flex align-items="center" style="padding-bottom: 34px;">
          <span style="margin-right: 16px;">Статус:</span>
          <mu-radio v-model="status" style="margin-right: 16px;" value='' label="Все"></mu-radio>
          <mu-radio v-model="status" style="margin-right: 16px;" value='true' label="Зачислены"></mu-radio>
          <mu-radio v-model="status" style="margin-right: 16px;" value='false' label="Не зачислены"></mu-radio>
        </mu-flex>
        <mu-col span="12" lg="4" sm="6" align="left">
          <mu-select label="Программа обучения" v-model="program" full-width>
            <mu-option label="Все" value=""></mu-option>
            <mu-option v-for="option in programs" :key="option.name" :label="option.name" :value="option.id"></mu-option>
          </mu-select>
              <p>Количесвтво: {{abits.length}}</p>
          <mu-button @click="printElem" color="primary">Скачать список</mu-button>
        </mu-col>
        <h1>Абитуриенты</h1>

      </mu-container>

        <mu-paper :z-depth="1">
          <mu-data-table id="table" :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="abits" >
            <template slot="expand" slot-scope="prop">
              <div style="padding: 24px;" >
                <mu-list>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Фамилия: {{prop.row.surname}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Имя: {{prop.row.name}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Отчество: {{prop.row.secondname}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Тип документа: {{shared.dict_doc[prop.row.document_type]}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Номер документа: {{prop.row.document_number}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Дата выпуска: {{prop.row.study_date}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>
                  Тип награды: {{shared.dict_award[prop.row.award_type]}}
                </mu-list-item-title></mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Тип обучения: {{shared.dict_student_type[prop.row.study_type]}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Форма обучения: {{shared.dict_contract[prop.row.contract_type]}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                  <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Тип поступления: {{shared.dict_abit_type[prop.row.abit_type]}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Особенности студента: {{shared.dict_student_type[prop.row.student_type]}}</mu-list-item-title>
                  </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Учебная программа: </mu-list-item-title></mu-list-item-content><mu-col span="12" lg="9" sm="6"><mu-select @change="changeProgram(prop.row.id, prop.row.study_program.id)" label=" " v-model="prop.row.study_program.id" full-width>
                    <mu-option v-for="option in programs" :key="option.name" :label="option.name" :value="option.id"></mu-option>
                </mu-select></mu-col></mu-list-item>

                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Сумма оценок: {{prop.row.marks}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Место учебы: {{prop.row.study_place.name}} {{prop.row.study_place.place}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-list-item-title>Зачислен: {{shared.dict_bool[prop.row.accepted]}}</mu-list-item-title>
                </mu-list-item-content></mu-list-item>
                <mu-list-item><mu-list-item-content>
                  <mu-button v-if="!prop.row.accepted" @click="setAbit(prop.row.id, !prop.row.accepted)" color="success">Зачислить</mu-button>
                  <mu-button v-if="prop.row.accepted" @click="setAbit(prop.row.id, !prop.row.accepted)" color="success">Отчислить</mu-button>
                </mu-list-item-content></mu-list-item>
                </mu-list>
              </div>
            </template>
            <template slot-scope="scope">
              <td>{{scope.row.surname}}</td>
              <td>{{scope.row.name}}</td>
              <td>{{scope.row.secondname}}</td>
              <td width="200">
                <mu-chip class="demo-chip" color="grey">
                  {{shared.dict_award[scope.row.award_type]}}
                 </mu-chip>
              </td>
              <td>{{shared.dict_study_type[scope.row.study_type]}}</td>
              <td>{{shared.dict_student_type[scope.row.student_type]}}</td>
              <td>{{scope.row.marks}}</td>
              <td>{{shared.dict_bool[scope.row.accepted]}}</td>
            </template>
          </mu-data-table>
        </mu-paper>
    </div>
</template>

<script>
    import $ from 'jquery'

    const shared = {dict_place: {1: 'Школа', 2: 'Колледж'},
                    dict_doc: {1: 'Паспорт', 2: 'Свидетельство о рождении'},
                    dict_award: {1: 'Нет', 2: 'Серебрянная медаль', 3: 'Золотая медаль'},
                    dict_contract: {1: 'Бюджет', 2: 'Платный'},
                    dict_abit_type: {1: 'После 9', 2: 'После 11'},
                    dict_student_type: {1: 'Нет', 2: 'Целевик', 3: 'Инвалид', 4: 'Сирота'},
                    dict_study_type: {1: 'Очная', 2: 'Очно-заочная', 3: 'Заочная'},
                    dict_bool: {false: 'Нет', true: 'Да'}}

    export default {
      name: "Abits",
      data() {
        return {
          shared,
          options: [
            'Option 1', 'Option 2', 'Option 3', 'Option 4',
            'Option 5', 'Option 6', 'Option 7', 'Option 8',
            'Option 9', 'Option 10'
          ],
          program: '',
          programs: [],
          contract: '0',
          form: '0',
          type: '0',
          status: '',
          places: ['1', '2'],
          place: '',
          all_abits: [],
          sort: {
            name: '',
            order: 'asc'
          },
          columns: [
            { title: 'Фамилия', name: 'surname' },
            { title: 'Имя', name: 'name' },
            { title: 'Отчество', name: 'secondname' },
            { title: 'Награда', name: 'award_type', width: 225},
            { title: 'Тип обучения', name: 'study_type', width: 140},
            { title: 'Особенности', name: 'student_type' },
            { title: 'Сумма оценок', name: 'marks', sortable: true },
            { title: 'Зачислен', name: 'accepted' },
          ],
        }
      },
      computed: {

        abits() {
          var result = this.all_abits

          var type = this.type
          var form = this.form
          var contract = this.contract
          var program = this.program
          var status = this.status

          console.log(this.program)
          result = result.filter(function(i) {
            if (contract != 0) {return i.contract_type == contract} else {return true}
          })
          result = result.filter(function(i) {
            if (type != 0) {return i.abit_type == type} else {return true}
          })
          result = result.filter(function(i) {
            if (form != 0) {return i.study_type == form} else {return true}
          })
          result = result.filter(function(i) {
            if (program != "") {return i.study_program.id == program} else {return true}
          })
          result = result.filter(function(i) {
            if (status != "") {return i.accepted.toString() == status} else {return true}
          })
          return result
        }
      },
      created() {
        $.ajaxSetup({
           headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadPrograms()
        this.loadAbits()
      },
      methods: {
        printElem() {
            var mywindow = window.open('', 'PRINT', 'height=400,width=600');
            var program = this.programs.find(item => item.id == this.program)
            var program_name = ""
            if (typeof program !== 'undefined') { program_name = program.name }
            mywindow.document.write('<html><head><title>' + "Список абитуриентов "  + program_name + '</title>');
            mywindow.document.write('</head><body >');
            mywindow.document.write('<h1>' + "Список абитуриентов "  + program_name  + '</h1>');
            mywindow.document.write(document.getElementById("table").innerHTML);
            mywindow.document.write('</body></html>');

            mywindow.document.close(); // necessary for IE >= 10
            mywindow.focus(); // necessary for IE >= 10*/

            mywindow.print();
            mywindow.close();

            return true;
        },
        handleSortChange ({name, order}) {
          console.log('name, order')
          this.list = this.abits.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
        },
        changeProgram(id_abit, id_program) {

          $.ajax({
                    url: "http://127.0.0.1:8000/api/setabitprogram/" + id_abit.toString() + "/",
                    type: "POST",
                    data: {
                        id_program: id_program,
                    },
                    success: (response) => {
                      alert("Обновление программы обучения прошло успешно!")
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ошибка!")
                        }
                    }
                })
        },
        setAbit(id, state) {
          $.ajax({
                    url: "http://127.0.0.1:8000/api/setabitstatus/" + id.toString() + "/",
                    type: "POST",
                    data: {
                        status: state,
                    },
                    success: (response) => {
                      alert("Обновление статуса прошло успешно!")
                      window.location = '/'
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Ошибка!")
                        }
                    }
                })
        },
        loadAbits() {
          $.ajax({
            url: "http://127.0.0.1:8000/api/abits/",
            type: "GET",
            success: (response) => {
              this.all_abits = response.data.values
            }
          })
        },
        loadPrograms() {
          $.ajax({
            url: "http://127.0.0.1:8000/api/programs/",
            type: "GET",
            success: (response) => {
              this.programs = response.data.values
            }
          })
        },
      },
    }
</script>

<style scoped>

</style>
