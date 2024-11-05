import Input from "../../props/input";
function LoginIndex(){
    return (
    <div className="w-[100vw] h-[100vh] m-0 bg-gradient-to-tr from-slate-800 via-blue-900 to-slate-800 justify-items-center place-content-center align-middle grid">
        <div className="w-[20rem] h-[27rem] sm:w-[20rem] sm:h-[18rem]  bg-black bg-opacity-40 backdrop-blur-3xl border-solid border-[.1rem] border-black rounded-2xl flex flex-col">
            <h1 className="w-full text-3xl text-center text-white font-bold my-4">Login</h1>
            <Input sttgs_type="email"></Input>
            <Input sttgs_type="password"></Input>
            <button className="bg-blue-600 text-white w-[80%] h-[2rem] rounded ml-[10%] mt-[5%]">Confirmar</button>
            <a className="w-full text-blue-300 text-[.9rem] text-center align-middle h-5 my-4 opacity-50" href="/register">Register instead</a>
        </div>
    </div>
    );
}
export default LoginIndex;