import { Component, OnInit } from '@angular/core';
import { KeepService } from 'src/app/services/keep.service';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  todo: any;
  currentTodo = null;
  currentIndex = -1;
  title = '';

  constructor(private todoService: KeepService) { }

  ngOnInit(): void {
    this.retrieveTodo();
  }

  retrieveTodo(): void {
    this.todoService.getAll()
      .subscribe(
        data => {
          this.todo = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveTodo();
    this.currentTodo = null;
    this.currentIndex = -1;
  }

  setActiveTodo(todo, index): void {
    this.currentTodo = todo;
    this.currentIndex = index;
  }

  removeAllTodo(): void {
    this.todoService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.retrieveTodo();
        },
        error => {
          console.log(error);
        });
  }

  searchTitle(): void {
    this.todoService.findByTitle(this.title)
      .subscribe(
        data => {
          this.todo = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
}
