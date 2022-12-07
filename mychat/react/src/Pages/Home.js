import React, { useState,useEffect } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
// import useWebSocket, { ReadyState } from 'react-use-websocket';
function Home() {
  const [data, setData] = useState([])
  const [socket, setSocket] = useState()
  // let url = `ws://${window.location.host}/ws/socket-server/`
  // const [socketUrl, setSocketUrl] = useState(`ws://${window.location.host}/ws/socket-server/`);







  useEffect(()=>{



getdata();
  },[])
  async function getdata(){

    let con = new WebSocket(`ws://127.0.0.1:8000/ws/socket-server/`)
    con.onopen = e =>{
      console.log('open',e)
    }
    con.onmessage = e=>{
      console.log("message")
      console.log(JSON.parse(e.data))
      let d= JSON.parse(e.data)
      console.log(d['message'])
      setData(d['message'])
    }
    con.onerror= e=>{
      console.log("error")
    }





// await axios.get("http://127.0.0.1:8000").then(
//   (responce)=>{
//     console.log(responce)
//   }
// ).catch((error)=>{
//   console.log(error)
// })



  }
  return (
    <div className='bg-primary'><h1>Home</h1>Home
    
    {
      data ? <p>data</p>:<p>nodata</p>

    }

    <div className='container '>
      <div className='row'>
      {
      data.map((bay_data,index)=>{
        return(<div className='col' key={index}>
          <div>{bay_data.id}
            </div>
            <div>{bay_data.bay_number}</div>
            <div className={`${bay_data.status==="Free"? "bg-success":"bg-warning"}`}>{
            
            bay_data.status}</div>
          
          
          
          </div>)
      }
  
      )
    }
      </div>

    </div>

    </div>
  )
}

export default Home