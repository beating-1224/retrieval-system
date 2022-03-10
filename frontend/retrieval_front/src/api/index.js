import axios from "axios"
// import Qs from 'qs'

const api = {
    getDatasets() {
        return axios.get("/api/datasets");
    },
    // getDatasets(params) {
    //     let readyData = Qs.stringify({
    //         username: params.username,
    //         password: params.password,
    //         email: params.email
    //     });
    //     return axios.post("/api/v1/register", readyData);
    // },
}

export default api;