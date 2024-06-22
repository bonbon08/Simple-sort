pub fn sort_own<T: PartialOrd>(mut input: Vec<T>) -> Vec<T> {
    let mut change = true;
    while change {
        change = false;
        for i in 1..input.len() {
            if input[i - 1] > input[i] {
                input.swap(i - 1, i);
                change = true;
            }
        }
    }
    input
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let mut vector = Vec::new();
        let mut seed: i64 = 29;
        for _ in 0..10000 {
            seed = (1664525 * seed + 1013904223) % 2i64.pow(32);
            vector.push(-10000 + (seed % (10000 - (-10000) + 1)));
        }
        let nvector = sort_own(vector);
        for i in nvector {
            println!("{}", i);
        }
    }
}

