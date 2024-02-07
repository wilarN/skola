
inquirer
    .prompt([
        {
            type: 'input',
            name: 'text',
            message: 'Enter the text for the QR code:',
        },
    ])
    .then((answers) => {
        const qrPng = qrImg.image(answers.text, { type: 'png' });
        qrPng.pipe(require('fs').createWriteStream('qr.png'));
    });