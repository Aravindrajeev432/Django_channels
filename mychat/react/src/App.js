import {BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import Create from './Pages/Create';
import Home from './Pages/Home';
function App() {
  return (
    <div className="App">
     <Router>
      <Routes>
        <Route path="/" element={<Home/>}></Route>
        <Route path="/create" element={<Create></Create>}></Route>
      </Routes>
     </Router>
    </div>
  );
}

export default App;
