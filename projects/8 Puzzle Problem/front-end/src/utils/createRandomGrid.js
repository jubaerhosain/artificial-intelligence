function shuffleArray(array) {
    const length = array.length;

    for (let i = length - 1; i > 0; i--) {
        // Generate a random index between 0 and i (inclusive)
        const randomIndex = Math.floor(Math.random() * (i + 1));

        // Swap elements at current index and random index
        [array[i], array[randomIndex]] = [array[randomIndex], array[i]];
    }

    return array;
}

function createRandomDistinctArray() {
    let array = shuffleArray([0, 1, 2, 3, 4, 5, 6, 7, 8]);
    array = shuffleArray(array);

    const matrix = [];
    for (let i = 0; i < 3; i++) {
        matrix.push(array.slice(i * 3, i * 3 + 3));
    }

    return matrix;
}

export default createRandomDistinctArray;
