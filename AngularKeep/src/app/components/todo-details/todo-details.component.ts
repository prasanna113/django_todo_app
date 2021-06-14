import { Component, OnInit } from '@angular/core';
import { KeepService } from 'src/app/services/keep.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-todo-details',
  templateUrl: './todo-details.component.html',
  styleUrls: ['./todo-details.component.css']
})
export class TodoDetailsComponent implements OnInit {

  currentTodo = null;
  message = '';

  constructor(
    private todoService: KeepService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    this.message = '';
    this.getTodo(this.route.snapshot.paramMap.get('id'));
  }

  getTodo(id): void {
    this.todoService.get(id)
      .subscribe(
        data => {
          this.currentTodo = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  updateStatus(status): void {
    const data = {
      title: this.currentTodo.title,
      status: status
    };

    this.todoService.update(this.currentTodo.id, data)
      .subscribe(
        response => {
          this.currentTodo.status = status;
          console.log(response);
        },
        error => {
          console.log(error);
        });
  }

  updateTodo(): void {
    this.todoService.update(this.currentTodo.id, this.currentTodo)
      .subscribe(
        response => {
          console.log(response);
          this.message = 'The todo was updated successfully';
        },
        error => {
          console.log(error);
        });
  }

  deleteTodo(): void {
    this.todoService.delete(this.currentTodo.id)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/todo']);
        },
        error => {
          console.log(error);
        });
  }
}
