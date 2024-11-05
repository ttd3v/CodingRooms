import PropTypes from 'prop-types';
import React, { useState } from 'react';

interface settings {
    state: 'empty' | 'wrong' | 'correct';
    value?: string;
    type: 'email' | 'password' | 'text';
}

let email_regexp = new RegExp(
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
);

type props_i = {
    sttgs_type: 'email' | 'password' | 'text';
};

function MyInput(props: props_i) {
    let settings: settings = {
        state: 'empty',
        type: props.sttgs_type,
    };

    const [inputStyle, setInputStyle] = useState(
        'w-[90%] ml-[5%] mr-[5%] text-center outline-none text-white rounded-md h-8 my-3 bg-black bg-opacity-60 border-solid border-[1px] border-gray-900'
    );

    const handleInput = (event: React.FormEvent<HTMLInputElement>) => {
        const target = event.target as HTMLInputElement;
        settings.value = target.value;

        if (target.value.length === 0) {
            settings.state = 'empty';
        } else if (target.value.length > 0) {
            if (target.type === 'email') {
                settings.state = email_regexp.test(target.value) ? 'correct' : 'wrong';
            }
            if (target.type === 'password') {
                settings.state = target.value.replaceAll(' ', '').length >= 8 ? 'correct' : 'wrong';
            }
        }

        if (settings.state === 'correct') {
            setInputStyle(
                'w-[90%] text-center ml-[5%] mr-[5%] outline-none rounded-md h-8 my-3 bg-black bg-opacity-60 border-solid border-[1px] text-green-500 border-green-500'
            );
        } else if (settings.state === 'wrong') {
            setInputStyle(
                'w-[90%] text-center ml-[5%] mr-[5%] outline-none rounded-md h-8 my-3 bg-black bg-opacity-60 border-solid border-[1px] text-red-500 border-red-500'
            );
        } else {
            setInputStyle(
                'w-[90%] text-center ml-[5%] mr-[5%] outline-none rounded-md h-8 my-3 bg-black bg-opacity-60 border-solid border-[1px] border-gray-900 text-white border-white'
            );
        }
    };
    let placeholders = {
        'email' : "Email",
        'password' : "Password",
        'text' : 'Text',
    }
    return <input className={inputStyle} placeholder={placeholders[settings.type]} type={settings.type} onInput={handleInput} />;
}

MyInput.propTypes = {
    sttgs_type: PropTypes.string,
};
MyInput.defaultProps = {
    sttgs_type: 'text',
};

export default MyInput;
