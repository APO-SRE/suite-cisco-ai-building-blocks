from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.br_backup_info import BrBackupInfo
from ...models.br_error_response import BrErrorResponse
from ...models.get_api_action_class_backuprestore_backup_name_action import (
    GetApiActionClassBackuprestoreBackupNameAction,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    action: Union[Unset, GetApiActionClassBackuprestoreBackupNameAction] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_action: Union[Unset, str] = UNSET
    if not isinstance(action, Unset):
        json_action = action.value

    params["action"] = json_action

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/action/class/backuprestore/backup/{name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BrBackupInfo, BrErrorResponse]]:
    if response.status_code == 200:
        response_200 = BrBackupInfo.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = BrErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = BrErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = BrErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BrBackupInfo, BrErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    action: Union[Unset, GetApiActionClassBackuprestoreBackupNameAction] = UNSET,
) -> Response[Union[Any, BrBackupInfo, BrErrorResponse]]:
    """Get details for a backup / Download a backup file

    Args:
        name (str):
        action (Union[Unset, GetApiActionClassBackuprestoreBackupNameAction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BrBackupInfo, BrErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        action=action,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    action: Union[Unset, GetApiActionClassBackuprestoreBackupNameAction] = UNSET,
) -> Optional[Union[Any, BrBackupInfo, BrErrorResponse]]:
    """Get details for a backup / Download a backup file

    Args:
        name (str):
        action (Union[Unset, GetApiActionClassBackuprestoreBackupNameAction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BrBackupInfo, BrErrorResponse]
    """

    return sync_detailed(
        name=name,
        client=client,
        action=action,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    action: Union[Unset, GetApiActionClassBackuprestoreBackupNameAction] = UNSET,
) -> Response[Union[Any, BrBackupInfo, BrErrorResponse]]:
    """Get details for a backup / Download a backup file

    Args:
        name (str):
        action (Union[Unset, GetApiActionClassBackuprestoreBackupNameAction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BrBackupInfo, BrErrorResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        action=action,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    action: Union[Unset, GetApiActionClassBackuprestoreBackupNameAction] = UNSET,
) -> Optional[Union[Any, BrBackupInfo, BrErrorResponse]]:
    """Get details for a backup / Download a backup file

    Args:
        name (str):
        action (Union[Unset, GetApiActionClassBackuprestoreBackupNameAction]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BrBackupInfo, BrErrorResponse]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            action=action,
        )
    ).parsed
