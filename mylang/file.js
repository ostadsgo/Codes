

/* 
 * Operators
 * **
 / // /% 
 % %%
 + ++
 - --
*/

/* aliase of a type */
Contacts := List[List[Str]];

/* Make an array */
numbers := [1, 2, 3];
numbers[0] = 10;
numbers := array(int, 10, [1, 2, 3]);  /* [1, 2, 3, 0, 0, 0, 0, 0, 0, 0] */
numbers: [int, 10];
numbers: [int, 10] = [1, 2, 3];

/* map */
person := ["name": "John", "age": 12];
person := map(str: str|int, ...);
person: [str: str|int, ...];

