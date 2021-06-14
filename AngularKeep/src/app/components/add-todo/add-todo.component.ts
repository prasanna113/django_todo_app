import { Component, OnInit } from '@angular/core';
import { KeepService } from 'src/app/services/keep.service'

@Component({
  selector: 'app-add-todo',
  templateUrl: './add-todo.component.html',
  styleUrls: ['./add-todo.component.css']
})
export class AddTodoComponent implements OnInit {

  todo = {
    title: '',
    status: false,
    due_date: ''
  };

  submitted = false;

  constructor(private keepService: KeepService) { }

  ngOnInit(): void {
  }

  saveTodo(): void {
    const data = {
      title: this.todo.title,
      due_date: this.todo.due_date
    };


  this.keepService.create(data)
    .subscribe(
      response=> {
        console.log(response);
        this.submitted = true;
      },

      error => {
        console.log(error);
      });
  }

  newTodo(): void {
    this.submitted = false;
    this.todo = {
      title: '',
      status: false,
      due_date: ''
    };
  }

}
