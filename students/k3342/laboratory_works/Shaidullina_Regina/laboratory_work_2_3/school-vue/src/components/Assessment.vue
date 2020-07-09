    <template>
    <mu-container><br>
        <mu-container class="button-wrapper2">
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="upd">Update</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="add">Add</mu-button>
            <mu-button v-if="auth" color="#5c6bc0" textColor="white" @click="del">Delete</mu-button><br><br>
        </mu-container>
        <mu-container>
            <mu-paper>
                <mu-data-table border :columns="columns" :data="assessment">
                    <template slot-scope="scope">
                        <td class="is-left">{{ scope.row.term }}</td>
                        <td class="is-left">{{ scope.row.pupil }}</td>
                        <td class="is-left">{{ scope.row.subject }}</td>
                        <td class="is-left">{{ scope.row.grade }}</td>
                    </template>
                </mu-data-table>
            </mu-paper>
            <br><br>
        </mu-container>
    </mu-container>
</template>

<script>
/* eslint-disable */

export default {
    name: 'Assessment',
    data() {
        return {
            assessment: '',
            columns: [
                { title: 'Term', name: 'term', align: 'center' },
                { title: 'Pupil', name: 'pupil', width: '370', align: 'center' },
                { title: 'Subject', name: 'subject', align: 'center' },
                { title: 'Grade', name: 'grade', align: 'center' },
            ]
        }
    },
    computed: {
        auth() {
            if (sessionStorage.getItem("auth_token")) {
                return true
            }
        }
    },
    created() {
        $.ajaxSetup({
            headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
        });
        this.loadAss()
    },
    methods: {
        returnHome() {
            window.location = '/'
        },
        add() {
            this.$router.push({name: "assessments_add"})
        },
        upd() {
            this.$router.push({name: "assessments_edit"})
        },
        del() {
            this.$router.push({name: "assessments_delete"})
        },
        loadAss() {
            $.ajax({
                url: "http://127.0.0.1:8000/school/assessments/",
                type: "GET",
                success: (response) => {
                    this.assessment = response.data.data
                }
            })
        }
    }
}
</script>

<style scoped>
    h2 {
        font-size: 48px; 
        font-weight: 400;
        text-align: center;
        color: #1a237e;
    },
    .button-wrapper2 {
        text-align: center;
        .mu-button{
            margin: 8px;
        }
    }
</style>
